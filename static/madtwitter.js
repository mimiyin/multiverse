/*
 * Copyright (c) 2009 Katie Capps Parlante
 */

function slideAnimation(element, callback) {
	var divHeightPx = element.css("height");
	var divHeight = element.height();
	var newTop = divHeight + 100;
	
	element.css({opacity:1.0, height:0, top:newTop});
    element
		.animate({height:divHeight, top:100}, "slow")
		.animate({opacity:1.0}, 2000)
		.animate({height:0}, "slow", function(){
			$('.stanza').css({opacity:0.0, height:divHeightPx, top:100});
			callback();
		});
}

function sideways(element, callback) {
    var firstLine = element.find('div:eq(0)');
    var secondLine = element.find('div:eq(1)');
    var thirdLine = element.find('div:eq(2)');

    var elementWidth = element.width();
    var firstLineWidth = firstLine.width();
    var secondLineWidth = secondLine.width();
    var thirdLineWidth = thirdLine.width();

    firstLine.css({marginLeft:-firstLineWidth});
    secondLine.css({marginLeft:elementWidth});
    thirdLine.css({marginLeft:-thirdLineWidth});
    element.css({opacity:1});

    firstLine.animate({marginLeft:0}, 1500, function(){
        secondLine.animate({opacity:1}).animate({marginLeft:0}, 1500, function(){
            thirdLine.animate({opacity:1}).animate({marginLeft:0}, 1500).animate({opacity:1}, 3000, function() {
            	firstLine.animate({marginLeft:elementWidth}, 1500, function(){
    				secondLine.animate({opacity:1}).animate({marginLeft:-secondLineWidth}, 1500, function(){
    					thirdLine.animate({opacity:1}).animate({marginLeft:elementWidth}, 1500, callback);
    				});
    			});
    		});
        });
    });		


}

function fadeSearchAnimation(element, callback) {
	element
		.fadeIn("slow")
		.animate({opacity:1.0}, 3000, function(){
			$(this).find('.search')
			.animate({opacity:0}, 3000, function(){
				$(this).parent().find('.tweet')
				.animate({opacity:1.0}, 3000, function(){
					$(this).animate({opacity:0}, "slow", function(){
						if ($(this)[0] === $('.tweet:last')[0]) {
							callback();
						}
					});
				});
			});
		});
}
	
function dropAnimation(element, callback) {
	element.fadeIn("slow")
		.animate({opacity:1.0}, 2000)
		.animate({
			opacity:0,
			top: $(window).height() - element.height()
		}, "slow", callback);
}

function spantext(phrase) {
	var newtext = "";
	
	// Made search global so it searches and replaces all
	phrase = phrase.replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
	
	//phrase = phrase.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'");
	for (var i=0; i < phrase.length; i++) {
	    if (phrase.charAt(i) != ' ') {
		    newtext = newtext.concat("<span class='letter'>" + phrase.charAt(i) + "</span>");
		} else {
		    newtext = newtext.concat(" ");
		}
	}
	return newtext;
}

function fadeLetter(element, callback) {
	var line = element.find('div:eq(3) .tweet');
	var html = line.html();
	
	line.html(spantext(html));
	
	var seconds = 0;
	
	element.animate({opacity:1.0}, "slow")
		.animate({opacity:1.0}, 2000, function(){
			$(this).find("span.letter").animate({opacity:1.0}, 5, function(){
				seconds = 100 + Math.floor(Math.random() * 3000);
				$(this).animate({opacity:1.0}, seconds).animate({opacity:0}, "slow")
			});
			$(this).animate({opacity:1.0}, 4000).animate({opacity:0}, "slow", function(){
				line.html(html);
				callback();
			});
		});
}

function projectionAnimation(element, callback) {
	
	//Dynamically calculate width/height of poem
	//Set margins accordingly to center poem	
	var phrase = element.find(".phrase");
	var longest = Math.max($(phrase[0]).text().length, $(phrase[1]).text().length, $(phrase[2]).text().length);
	element.find(".phrase").css('font-size', 200/longest + 'vw');

	// Show tweeters
	// if(element.find("input[name=user1]") && element.find("input[name=user1]").val().length > 0) {
	// 	var tweeters = $("<div>").addClass("tweeters").text('@' + element.find("input[name=user1]").val() + ', @' + element.find("input[name=user2]").val() + ', @' + element.find("input[name=user3]").val());
	// 	element.append(tweeters);
	// 	setTimeout(function(){ tweeters.fadeTo(5000, .34) }, 1000);
	// }

    element.find('.tweet, .search').each(function(){
        var html = $(this).html();
        
        $(this).data("old", html);
        $(this).html(spantext(html));
    });

    $("#poem").width(element.width());
    
    var seconds = 0;
    var holdLength = 500;
    
    element.find("span.letter").css({opacity:0});
    element.css({opacity:1, 'display':'block'});
    
    element.find("span.letter").each(function(){
        seconds = 100 + Math.floor(Math.random() * 3000);
        $(this).animate({opacity:0}, seconds).animate({opacity:1.0}, "slow")
    });

    element.animate({opacity:1.0}, 6000, function() {
        $(this).find("span.letter").animate({opacity:1.0}, 4000, function(){
            seconds = 100 + Math.floor(Math.random() * 3000);
            $(this).animate({opacity:1.0}, seconds).animate({opacity:1.0}, holdLength).animate({opacity:0}, "slow")
        });
		$(this).animate({opacity:1.0}, 8000).animate({opacity:1.0}, holdLength).animate({opacity:0}, "slow", function(){
			element.find('.tweet, .search').each(function(){
				var old = $(this).data("old");
				$(this).html(old);
			});
			callback();
		});
    });
}

function fountain(element, callback) {
    
    $('#poem').css({
        'width' : element.width(),
    });

    $('#poem').find('.phrase').css('white-space','nowrap');
    // TODO: reconsider above
  
    element.find('.tweet, .search').each(function(){
        var html = $(this).html();
        
        $(this).data("old", html);
        $(this).html(spantext(html));
    });
    
    var seconds = 0;
    
    element.find("span.letter").css({opacity:0});
    element.css({opacity:1, 'display':'block'});
    
    element.find("span.letter").each(function(){
        seconds = 100 + Math.floor(Math.random() * 3000);
        $(this).animate({opacity:0}, seconds).animate({opacity:1.0}, "slow")
    });

    element.animate({opacity:1.0}, 6000, function() {
        $(this).find("span.letter").animate({opacity:1.0}, 4000, function(){
            seconds = 100 + Math.floor(Math.random() * 3000);
            $(this).animate({opacity:1.0}, seconds).animate({opacity:0}, "slow")
        });
        $(this).animate({opacity:1.0}, 8000).animate({opacity:0}, "slow", function(){
            element.find('.tweet, .search').each(function(){
              var old = $(this).data("old");
              $(this).html(old);
            });
            callback();
        });
    });
}


function fadeLines(element, callback) {
    var firstLine = element.find('div:eq(0)');
    var secondLine = element.find('div:eq(1)');
    var thirdLine = element.find('div:eq(2)');
    
    firstLine.css({opacity:0});
    secondLine.css({opacity:0});
    thirdLine.css({opacity:0});
    element.css({opacity:1});
    
    firstLine.animate({opacity:1.0}, "slow", function(){
        secondLine.animate({opacity:0}).animate({opacity:1.0}, "slow", function(){
            thirdLine.animate({opacity:0}).animate({opacity:1.0}, "slow").animate({opacity:1}, 2000, function() {
            	firstLine.animate({opacity:0}, "slow", function(){
    				secondLine.animate({opacity:1}).animate({opacity:0}, "slow", function(){
    					thirdLine.animate({opacity:1}).animate({opacity:0}, "slow", callback)
    				});
    			});
    		});
        });
    });		
}

function fadePair(element, callback) {
    var firstLine = element.find('div.line1');
    var secondLine = element.find('div.line2');
    
    firstLine.css({opacity:0});
    secondLine.css({opacity:0});
    element.css({opacity:1});
    
    firstLine.animate({opacity:1.0}, "slow", function(){
        secondLine.animate({opacity:0}).animate({opacity:1.0}, "slow").animate({opacity:1}, 4000, function() {
            firstLine.animate({opacity:0}, "slow", function(){
    			secondLine.animate({opacity:1}).animate({opacity:0}, "slow", callback)
    		});
        });
    });		
    
}

function cycle(animation) {
	if ($('div').length > 0) {
	    animation($('div:first'), function() {
            $('div:first').remove();
            cycle(animation);
        });
	} else {
		$('body').load('/tweets/', function() {
			$('.stanza').css({opacity:0});
			cycle(animation);
		});
	}
}

function cycleCustom(animation, search_one, search_two, search_three, page) {
	if ($('div').length > 0) {
	    animation($('div:first'), function() {
            $('div:first').remove();
            cycleCustom(animation, search_one, search_two, search_three, page);
        });
	} else {
	    var query = "?one=" + search_one + "&two=" + search_two + "&three=" + search_three + "&page=" + page
	    page += 1;
		$('body').load('/lines/' + query, function() {
			$('.stanza').css({opacity:0});
			cycleCustom(animation, search_one, search_two, search_three, page);
		});
	}
}

function fadeInOut(element) {
	element.fadeIn(10000, function(){
		element.fadeOut(5000, function(){
			fadeInOut(element);
		})
	})
}

function cycleRandom(title, animation, page) {
	if ($('div.stanza').length > 0) {
	    animation($('div.stanza:first'), function() {
            $('div.stanza:first').remove();
            cycleRandom(title, animation, page);
        });
	} else {
		var loading = $("<div>").attr("id", "loading").text("...Collecting Tweets...").prependTo($("body"));
		fadeInOut(loading);
	    if (page === 1000) return;
	    var query = "?page=" + page;
	    page += 1;
		$('#poem').load('/' + title + '.html' + query, function(responseText, textStatus) {
			$('div.stanza').css({opacity:0, 'display':'none'});
			loading.fadeOut("fast", function(){ loading.remove(); });
			cycleRandom(title, animation, page);
		});
	}
    
}

function cycleSelect(animation) {
	if ($('div.stanza').length > 0) {
	    animation($('div.stanza:first'), function() {
            $('div.stanza:first').remove();
            cycleSelect(animation);
        });
	} else {
		var loading = $("<div>").attr("id", "loading").text("Select Poems...").prependTo($("body"));
		fadeInOut(loading);
		setTimeout(function(){
			$('#poem').load('/select.html', function(responseText, textStatus) {
				$('div.stanza').css({opacity:0, 'display':'none'});
				loading.fadeOut("fast", function(){ loading.remove(); });
				cycleSelect(animation);
			});
		}, 2500)
	}
    
}

function fadeHeadline(callback) {
	var mult = 500;
	// Show tagline for every batch of poems
	$("#subtitle").fadeOut("fast", function(){
		$('#url')
			.fadeTo(2.5*mult, 1, function(){
				$("#headline").fadeTo(5*mult, 1, function(){
					setTimeout(function() {
					  	$("#headline").fadeTo(1*mult, 0, function(){
					  		$("#url").fadeTo(2.5*mult, 0, function(){
								$("#subtitle").fadeIn("slow", callback || null);
					  		});
						});
					}, 5*mult);
				});
			});
		});
}

var counter = 0;
function cycleProjection(animation, page) {
	var numPoems = $('div.stanza').length;

	var cycle = function() {
		counter++;
		var rand = Math.floor(Math.random()*numPoems);
		console.log("RAND", rand, numPoems);
	    animation($($('div.stanza')[rand]), function() {
	        //$($('div.stanza')[rand]).remove();
	        cycleProjection(animation);
	    });		
	}

	if (numPoems > 0) {
		if(counter%10 == 0) {
			fadeHeadline(function(){
				cycle();
			});
		}
		else {
			cycle();
		}
	} 
	// else {	
	//     fadeHeadline(function(){
	//     	var query = '';
 //    		var titles = [ 'select' ];
 //    		var tights = {};
 //    		var ready = 0;
 //    		$.each(titles, function(t,title){
 //    			var hold = $("<div>").attr("id", title).appendTo($("#hold"));
	// 			hold.load('/' + title + '.html' + query, function(responseText, textStatus) {
	// 				if(textStatus == "error") {
	// 					titles.splice(t, 1);
	// 					console.log(titles);
	// 				}
	// 				else {
	// 					console.log(title, $('div.stanza').length);
	// 					if(!(title in tights)) {
	// 						ready++;
	// 					}
	// 					tights[title] = true;
	// 					if( ready >= titles.length ) {
	// 						console.log("TITLE", title, ready);
	// 						$('#hold .stanza').appendTo($("#poem"));
	// 	                	cycleProjection(animation, page);
	// 					}
	// 				}
	// 			});
	//         });
 //    	}); 
 //    }  
}

  



