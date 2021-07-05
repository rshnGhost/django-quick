function CountDown(duration) {
  if (!isNaN(duration)) {
    var timer = duration, minutes, seconds;
    var interVal=  setInterval(function () {
      hours = parseInt(timer % ( 60 * 60 * 24) / ( 60 * 60), 10);
      minutes = parseInt(timer % ( 60 * 60) / 60, 10);
      seconds = parseInt(timer % 60, 10);
      hours = hours < 10 ? "0" + hours : hours;
      minutes = minutes < 10 ? "0" + minutes : minutes;
      seconds = seconds < 10 ? "0" + seconds : seconds;
      document.getElementById("sec").innerHTML=seconds;
      document.getElementById("min").innerHTML=minutes;
      document.getElementById("hr").innerHTML=hours;
      if (--timer < 0) {
        timer = duration;
        document.getElementById("formId").submit();
        clearInterval(interVal)
      }
    },1000);
  }
}
