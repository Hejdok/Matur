<script>

    let elapsedTime = $state(0)

    // setTimeout(funcke, 1000)
    setInterval(function(){
        elapsedTime +=1
    }, 1000)

</script>

<p>Time: {elapsedTime}</p>