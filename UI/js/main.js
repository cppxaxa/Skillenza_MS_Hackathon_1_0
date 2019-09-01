apiLink = "http://127.0.0.1:3000";

function reOrg()
{
//     width = $("#mental_health_index_indicator_parent_div").width();
//     $("#myChart-img").css('transform', 'scale(' + (width * 0.5) + ')');
//     $("#myChart").css('transform', 'scale(' + (width * 0.0025) + ')');
}

function explodePie (e) {
	if(typeof (e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
	} else {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
	}
	e.chart.render();
    e.chart1.render();
    e.chart2.render();
    e.chart3.render();
}


$(document).ready(function() {
    $(document).ready(function() {
        reOrg();

        var chart = new CanvasJS.Chart("chartContainer", {
            theme: "light2",
            exportEnabled: true,
            animationEnabled: true,
            exportEnabled: false,
            title:{
                //text: "State Operating Funds"
            },
            legend:{
                cursor: "pointer",
                itemclick: explodePie
            },
            data: [{
                indexLabelFontSize: 15,
                indexLabelFontWeight: "bold",
                type: "pie",
                showInLegend: true,
                toolTipContent: "{name}: <strong>{y}%</strong>",
                indexLabel: "{name} - {y}%",
                dataPoints: [
                    { y: 26, name: "Avg. Positive", exploded: true },
                    { y: 20, name: "Avg. Negative" }
                ]
            }]
        });


        
        var chart1 = new CanvasJS.Chart("chartContainer1", {
            theme: "light2",
            animationEnabled: true, 
            exportEnabled: false,
            title:{
                //text: "State Operating Funds"
            },
            data: [{
                type: "doughnut",
                startAngle: 60,
                //innerRadius: 60,
                indexLabelFontSize: 17,
                indexLabel: "{label} - #percent%",
                toolTipContent: "<b>{label}:</b> {y} (#percent%)",
                dataPoints: [
                    { y: 67, label: "Co-workers" },
                    { y: 58, label: "Supervisor" },
                    { y: 70, label: "Mental Health Interview" },
                    { y: 42, label: "Physical Health Interview" }
                ]
            }]
        });

        var chart2 = new CanvasJS.Chart("chartContainer2", {
            theme: "light2",
            
            animationEnabled: true,
            exportEnabled: false,
            title:{
                //text: "State Operating Funds"
            },
            legend:{
                cursor: "pointer",
                itemclick: explodePie
            },
            data: [{
                indexLabelFontSize: 15,
                indexLabelFontWeight: "bold",
                type: "pie",
                showInLegend: true,
                toolTipContent: "{name}: <strong>{y}%</strong>",
                indexLabel: "{name} - {y}%",
                dataPoints: [
                    { y: 26, name: "Benefits", exploded: true },
                    { y: 29, name: "Seek Help" },
                    { y: 31, name: "Care Options" },
                    { y: 41, name: "Wellness Programmes" },
                    { y: 38, name: "Anonymity" },
                    { y: 35, name: "Leave" }
                ]
            }]
        });

        chart.render();
        chart1.render();
        chart2.render();




        $.urlParam = function (name) {
            var results = new RegExp('[\?&]' + name + '=([^&#]*)')
                              .exec(window.location.search);
        
            return (results !== null) ? results[1] || 0 : false;
        }
        
        snoQuery = $.urlParam('sno');
        submitQuery = $.urlParam('submit');
        if (snoQuery != false)
        {
        alert("Hello 1");

            console.log(snoQuery);
            link = apiLink + "/search_with_sno?sno=" + snoQuery;
    
            console.log(link);
    
            $.get(link, function(data) {
                console.log(data);
                
                $("#mandatory-user-details").hide();
                $("#Additional_Data_Grid").hide();
                $("#Additional_Data_Grid").hide();
                
                $("#BigInfoText").html(data['treatment']);
                $("#pieChart").html("Model Confidence");

                chart = new CanvasJS.Chart("chartContainer", {
                    theme: "light2",
                    exportEnabled: true,
                    animationEnabled: true,
                    exportEnabled: false,
                    title:{
                        //text: "State Operating Funds"
                    },
                    legend:{
                        cursor: "pointer",
                        itemclick: explodePie
                    },
                    data: [{
                        indexLabelFontSize: 15,
                        indexLabelFontWeight: "bold",
                        type: "pie",
                        showInLegend: true,
                        toolTipContent: "{name}: <strong>{y}%</strong>",
                        indexLabel: "{name} - {y}%",
                        dataPoints: [
                            { y: data['mental_index'], name: "Confident", exploded: true },
                            { y: 100 - data['mental_index'], name: "Unsure" }
                        ]
                    }]
                });

                chart.render();
    
                // $('#age_range option[value=' + data['age_range'] + ']').attr('selected','selected');
                // $("#age_range").prop('disabled', true);
                // $("#age_range").css('color', 'black');
                
                // $('#gender option[value=' + data['gender'] + ']').attr('selected','selected');
                // $("#gender").prop('disabled', true);
                // $("#gender").css('color', 'black');
                
                // $('#gender option[value=' + data['gender'] + ']').attr('selected','selected');
                // $("#gender").prop('disabled', true);
                // $("#gender").css('color', 'black');
                
                // //$('#gender option[value=' + data['gender'] + ']').attr('selected','selected');
                // $("#gender").prop('checked', true);
                // $("#gender").css('color', 'black');
                // $("#family_history").html("no");
            });
        }
        else if (submitQuery != false)
        {
        alert("Hello2");

            //alert("Form added");

            age_range=$.urlParam('age_range');
            gender=$.urlParam('gender');
            family_history=$.urlParam('family_history');
            wellness_program=$.urlParam('wellness_program');
            mental_health_consequence=$.urlParam('mental_health_consequence');
            phys_health_consequence=$.urlParam('phys_health_consequence');

            link = apiLink + "/add_new_row_to_db";
    
            console.log(link);
    
            $.get(link, function(data) {
                console.log(data);
                //alert(data);

                $("#BigInfoText").html(data['treatment']);

                chart = new CanvasJS.Chart("chartContainer", {
                    theme: "light2",
                    exportEnabled: true,
                    animationEnabled: true,
                    exportEnabled: false,
                    title:{
                        //text: "State Operating Funds"
                    },
                    legend:{
                        cursor: "pointer",
                        itemclick: explodePie
                    },
                    data: [{
                        indexLabelFontSize: 15,
                        indexLabelFontWeight: "bold",
                        type: "pie",
                        showInLegend: true,
                        toolTipContent: "{name}: <strong>{y}%</strong>",
                        indexLabel: "{name} - {y}%",
                        dataPoints: [
                            { y: data['mental_index'], name: "Confident", exploded: true },
                            { y: 100 - data['mental_index'], name: "Unsure" }
                        ]
                    }]
                });

                chart.render();

                window.location.href = "user.html?sno=" + data['sno'];
            });
        }
        else {
            link = apiLink + "/avg_mental_health_index";
    
            console.log(link);
    
            $.get(link, function(data) {
                console.log(data);

                $("#BigInfoText").html(data['avg_mental_index'] + "%");

                chart = new CanvasJS.Chart("chartContainer", {
                    theme: "light2",
                    exportEnabled: true,
                    animationEnabled: true,
                    exportEnabled: false,
                    title:{
                        //text: "State Operating Funds"
                    },
                    legend:{
                        cursor: "pointer",
                        itemclick: explodePie
                    },
                    data: [{
                        indexLabelFontSize: 15,
                        indexLabelFontWeight: "bold",
                        type: "pie",
                        showInLegend: true,
                        toolTipContent: "{name}: <strong>{y}%</strong>",
                        indexLabel: "{name} - {y}%",
                        dataPoints: [
                            { y: data['yes_no'], name: "Treatment", exploded: true },
                            { y: 100 - data['yes_no'], name: "Healthy" }
                        ]
                    }]
                });

                chart.render();
            });
        }




        var chart3 = AmCharts.makeChart("chartdiv", {
            "type": "gauge",
            "titles": [{
                "text": "Loaded Model Health: Current Accuracy",
                "size": 25
            }],
            "axes": [{
                "startValue": 0,
                "axisThickness": 1,
                "endValue": 100,
                "valueInterval": 10,
            
                "bottomText": "0%",
                "bands": [{
                    "startValue": 0,
                    "endValue": 40,
                    "color": "#ea3838"
                },
                {
                    "startValue": 40,
                    "endValue": 70,
                    "color": "#ffac29"
                },
                {
                    "startValue": 70,
                    "endValue": 100,
                    "color": "#00CC00",
                    
                    "innerRadius": "95%"
                }
                ]
            }],
            "arrows": [{}],
            "responsive": {
                "enabled": true
            }
        });
        
        //alert(chart3);
        setInterval(randomValue, 2000);
        // set random value
        function randomValue() {
            // alert("Hi");
            var value = 83;
            chart3.arrows[0].setValue(value);
            chart3.axes[0].setBottomText(value + " %");

            chart3.render();
        }

    });

    $(window).resize(function() { 
        reOrg();
    });
    // $("#mental_health_index_indicator_parent_div").resize(function() {
    //     alert("Hello");
    // });

    $("#search").keydown(function(e){
        if (e.keyCode == 13){
            window.location.href = 'user.html?sno=' + $("#search").val();
        }
    });
});

// function search_sno()
// {
//     alert(e);
// }