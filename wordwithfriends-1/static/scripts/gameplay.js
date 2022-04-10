// // Timer
// $(function() {
// 	var current_progress = 100;
// 	var interval = setInterval(function() {
// 		if ("{{opponent}}" != null) {
// 			current_progress -= 0.1;
// 			$("#dynamic")
// 			.css("width", current_progress + "%")
// 			.attr("aria-valuenow", current_progress)
// 			if (current_progress <= -2) {
// 				clearInterval(interval);
// 				location.href='/giveup/{{roomId}}/{{request.user.username}}'
// 			}
// 		}
// 	}, 50);
//   });

