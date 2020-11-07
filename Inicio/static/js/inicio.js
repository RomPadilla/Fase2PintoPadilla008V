var bg = ["Orange","Blue","Red","Purple","Black","Silver"]

function fondosRandom() {
var imgs = bg[Math.floor(Math.random()*bg.length)]
document.body.style.background= imgs ;

}

function PlayStop(){
	if(videos.paused){
		$("#play").css({'background':'yellow'});
		videos.play();
	}else{
		videos.pause();
		$("#play").css({'background':'Green'});
	};

};

function silence(){
	if(videos.muted){
		$("#mute").css({'background':'Green'});
		videos.muted = false;
	}else{
		videos.muted = true;
		$("#mute").css({'background':'yellow'});
	};

};

function adelanretro(value){
		videos.currentTime += value;
};


