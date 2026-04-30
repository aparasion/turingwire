/* ==========================================================================
   Turing Wire — stocks.js
   AIStocks dashboard: heatmap treemap + AI Index line chart using Apache ECharts
   ========================================================================== */

(function () {
  'use strict';

  // ECharts instances
  var heatmapChart = null;
  var indexChart = null;

  // Theme-aware colors
  function getThemeColors() {
    var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    return {
      bg:        isDark ? '#161615' : '#ffffff',
      text:      isDark ? '#ededed' : '#111110',
      muted:     isDark ? '#6b7280' : '#9ca3af',
      border:    isDark ? '#2a2a28' : '#e5e5e3',
      gridLine:  isDark ? '#1f1f1d' : '#f0f0ee',
      positive:  '#16a34a',
      negative:  '#dc2626',
      neutral:   isDark ? '#6b7280' : '#9ca3af',
      accent:    '#f97316',
    };
  }

  // ── Heatmap treemap ────────────────────────────────────────────────────────

  function buildHeatmapOption(data, colors) {
    // data: [{symbol, name, price, change_pct, market_cap_proxy}]
    var treeData = data.map(function (d) {
      var pct = d.change_pct || 0;
      var color;
      if (pct > 3)        color = '#15803d';
      else if (pct > 1.5) color = '#16a34a';
      else if (pct > 0)   color = '#22c55e';
      else if (pct < -3)  color = '#991b1b';
      else if (pct < -1.5) color = '#dc2626';
      else if (pct < 0)   color = '#ef4444';
      else                color = colors.neutral;

      return {
        name: d.symbol,
        value: Math.abs(d.price || 100),  // size = price as proxy
        label: d.symbol,
        pct: pct,
        price: d.price,
        fullName: d.name,
        itemStyle: { color: color },
      };
    });

    return {
      backgroundColor: 'transparent',
      tooltip: {
        trigger: 'item',
        backgroundColor: colors.bg,
        borderColor: colors.border,
        textStyle: { color: colors.text, fontFamily: 'JetBrains Mono' },
        formatter: function (params) {
          var d = params.data;
          if (!d.price) return '';
          var sign = d.pct >= 0 ? '+' : '';
          return [
            '<strong>' + d.label + '</strong> · ' + d.fullName,
            '$' + d.price.toFixed(2) + ' &nbsp; <span style="color:' + (d.pct >= 0 ? '#16a34a' : '#dc2626') + '">' + sign + d.pct.toFixed(2) + '%</span>',
          ].join('<br>');
        },
      },
      series: [{
        type: 'treemap',
        data: treeData,
        width: '100%',
        height: '100%',
        roam: false,
        nodeClick: false,
        breadcrumb: { show: false },
        label: {
          show: true,
          formatter: function (params) {
            var d = params.data;
            var sign = d.pct >= 0 ? '+' : '';
            return d.label + '\n' + sign + (d.pct || 0).toFixed(2) + '%';
          },
          color: '#ffffff',
          fontFamily: 'JetBrains Mono',
          fontSize: 11,
          fontWeight: 500,
        },
        itemStyle: {
          borderWidth: 2,
          borderColor: colors.bg,
          gapWidth: 2,
        },
        levels: [{
          itemStyle: {
            borderWidth: 3,
            borderColor: colors.bg,
            gapWidth: 3,
          },
        }],
      }],
    };
  }

  // ── AI Index line chart ────────────────────────────────────────────────────

  function buildIndexOption(series, range, colors) {
    // series: [{timestamp, value, change_pct}]
    var now = new Date();
    var cutoff;
    if (range === '1M') cutoff = new Date(now - 30 * 86400000);
    else if (range === '3M') cutoff = new Date(now - 90 * 86400000);
    else if (range === 'YTD') cutoff = new Date(now.getFullYear(), 0, 1);
    else if (range === '1Y') cutoff = new Date(now - 365 * 86400000);
    else cutoff = new Date(0); // YOY / all

    var filtered = series.filter(function (p) {
      return new Date(p.timestamp) >= cutoff;
    });

    var dates = filtered.map(function (p) { return p.timestamp.slice(0, 10); });
    var values = filtered.map(function (p) { return p.value; });
    var latest = values[values.length - 1] || 100;
    var first = values[0] || 100;
    var lineColor = latest >= first ? colors.positive : colors.negative;

    return {
      backgroundColor: 'transparent',
      grid: { left: 50, right: 16, top: 16, bottom: 32 },
      xAxis: {
        type: 'category',
        data: dates,
        axisLine: { lineStyle: { color: colors.border } },
        axisTick: { show: false },
        axisLabel: {
          color: colors.muted,
          fontFamily: 'JetBrains Mono',
          fontSize: 10,
          interval: Math.floor(dates.length / 5),
        },
      },
      yAxis: {
        type: 'value',
        axisLabel: {
          color: colors.muted,
          fontFamily: 'JetBrains Mono',
          fontSize: 10,
          formatter: function (v) { return v.toFixed(1); },
        },
        splitLine: { lineStyle: { color: colors.gridLine } },
        axisLine: { show: false },
        axisTick: { show: false },
      },
      tooltip: {
        trigger: 'axis',
        backgroundColor: colors.bg,
        borderColor: colors.border,
        textStyle: { color: colors.text, fontFamily: 'JetBrains Mono', fontSize: 12 },
        formatter: function (params) {
          var p = params[0];
          return p.axisValue + '<br><strong>' + p.value.toFixed(2) + '</strong>';
        },
      },
      series: [{
        type: 'line',
        data: values,
        smooth: false,
        symbol: 'none',
        lineStyle: { color: lineColor, width: 2 },
        areaStyle: {
          color: {
            type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
            colorStops: [
              { offset: 0, color: lineColor + '33' },
              { offset: 1, color: lineColor + '05' },
            ],
          },
        },
        markLine: {
          silent: true,
          symbol: 'none',
          lineStyle: { color: colors.muted, type: 'dashed', width: 1 },
          data: [{ yAxis: 100, label: { formatter: 'Base 100', color: colors.muted, fontSize: 10 } }],
        },
      }],
    };
  }

  // ── Initialize ─────────────────────────────────────────────────────────────

  function initHeatmap(stockData) {
    var el = document.getElementById('tw-heatmap');
    if (!el || typeof echarts === 'undefined') return;

    heatmapChart = echarts.init(el, null, { renderer: 'canvas' });
    var colors = getThemeColors();
    var quotes = Object.values(stockData.quotes || {});
    heatmapChart.setOption(buildHeatmapOption(quotes, colors));

    window.addEventListener('resize', function () { heatmapChart.resize(); });
  }

  function initIndexChart(historyData) {
    var el = document.getElementById('tw-index-chart');
    if (!el || typeof echarts === 'undefined') return;

    indexChart = echarts.init(el, null, { renderer: 'canvas' });
    var colors = getThemeColors();
    var currentRange = '3M';
    indexChart.setOption(buildIndexOption(historyData.series || [], currentRange, colors));

    // Range selector buttons
    document.querySelectorAll('[data-range]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        currentRange = btn.getAttribute('data-range');
        document.querySelectorAll('[data-range]').forEach(function (b) {
          b.classList.remove('active');
        });
        btn.classList.add('active');
        indexChart.setOption(buildIndexOption(historyData.series || [], currentRange, getThemeColors()), true);
      });
    });

    window.addEventListener('resize', function () { indexChart.resize(); });
  }

  // Re-render charts on theme change
  var observer = new MutationObserver(function () {
    if (heatmapChart) {
      var stockData = window._twStockData || {};
      heatmapChart.setOption(buildHeatmapOption(Object.values(stockData.quotes || {}), getThemeColors()), true);
    }
    if (indexChart) {
      var historyData = window._twIndexHistory || {};
      var currentRange = (document.querySelector('[data-range].active') || {}).getAttribute('data-range') || '3M';
      indexChart.setOption(buildIndexOption(historyData.series || [], currentRange, getThemeColors()), true);
    }
  });

  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-theme'],
  });

  // ── Bootstrap ──────────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', function () {
    var stockData = window._twStockData || {};
    var historyData = window._twIndexHistory || {};
    initHeatmap(stockData);
    initIndexChart(historyData);
  });

})();
