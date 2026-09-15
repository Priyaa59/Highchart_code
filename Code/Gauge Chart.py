GAUGE CHART CODE:
 
{
  "chart": {
    "type": "solidgauge",
    "height": "60%",
    "backgroundColor": "transparent"
  },
 
  "title": {
    "text": "Average Progress Percent",
     "style": {
        "fontSize": "18px",
        "fontWeight": "bold"
    }
  },
 
  "tooltip": {
    "enabled": false
  },
 
  "pane": {
    "startAngle": -90,
    "endAngle": 90,
    "center": ["50%", "85%"],
    "size": "150%",
    "background": [
      {
        "outerRadius": "100%",
        "innerRadius": "78%",
        "backgroundColor": "#E6E6E6",
        "borderWidth": 0,
        "shape": "arc"
      }
    ]
  },
 
  "yAxis": {
    "min": 0,
    "max": 100,
 
    "lineWidth": 0,
    "tickWidth": 0,
    "tickLength": 0,
    "minorTickLength": 0,
 
    "tickPositions": [0,20,40,60,80,100],
 
    "labels": {
      "distance": 15,
      "style": {
        "fontSize": "11px",
        "color": "#666666"
      }
    },
 
    "stops": [
      [0, "#8ECDF4"],
      [1, "#8ECDF4"]
    ]
  },
 
  "plotOptions": {
    "solidgauge": {
      "rounded": false,
      "linecap": "square",
      "dataLabels": {
        "enabled": true,
        "borderWidth": 0,
        "y": -5,
        "useHTML": true,
        "format": "<div style='text-align:center'><span style='font-size:28px;font-weight:bold'>{y}%</span></div>"
      }
    }
  },
 
  "series": [
    {
      "type": "solidgauge",
      "radius": "100%",
      "innerRadius": "78%",
      "name": "Progress",
      "data":["getColumn", 0]
    }
  ],
 
  "credits": {
    "enabled": false
  }
}

 
