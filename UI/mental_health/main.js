function mental_health(value) {
  let chartConfig = {
    type: 'gauge',
    globals: {
      fontSize: '25px'
    },
    plot: {
      valueBox: {
        text: '%v', // default
        fontSize: '35px',
        placement: 'center',
        rules: [
          {
            text: '%v<br>EXCELLENT',
            rule: '%v >= 700'
          },
          {
            text: '%v<br>Good',
            rule: '%v < 700 && %v > 640'
          },
          {
            text: '%v<br>Fair',
            rule: '%v < 640 && %v > 580'
          },
          {
            text: '%v<br>Bad',
            rule: '%v <  580'
          }
        ]
      },
      size: '100%'
    },
    plotarea: {
      marginTop: '80px'
    },
    scaleR: {
      aperture: 180,
      center: {
        visible: false
      },
      item: {
        offsetR: 0,
        rules: [
          {
            offsetX: '15px',
            rule: '%i == 9'
          }
        ]
      },
      labels: ['300', '', '', '', '', '', '580', '640', '700', '750', '', '850'],
      maxValue: 850,
      minValue: 300,
      ring: {
        rules: [
          {
            backgroundColor: '#E53935',
            rule: '%v <= 580'
          },
          {
            backgroundColor: '#EF5350',
            rule: '%v > 580 && %v < 640'
          },
          {
            backgroundColor: '#FFA726',
            rule: '%v >= 640 && %v < 700'
          },
          {
            backgroundColor: '#29B6F6',
            rule: '%v >= 700'
          }
        ],
        size: '50px'
      },
      step: 50,
      tick: {
        visible: false
      }
    },
    tooltip: {
      borderRadius: '5px'
    },
    // refresh: {
    //   type: 'feed',
    //   url: 'feed()',
    //   interval: 10000,
    //   resetTimeout: 1000,
    //   transport: 'js'
    // },
    series: [
      {
        values: [value], // starting value
        backgroundColor: 'black',
        indicator: [10, 10, 10, 10, 0.75],
        animation: {
          effect: 'ANIMATION_EXPAND_VERTICAL',
          method: 'ANIMATION_BACK_EASE_OUT',
          sequence: 'null',
          speed: 900
        }
      }
    ]
  };

  zingchart.render({
    id: 'myChart',
    data: chartConfig
  });
}

mental_health(300);