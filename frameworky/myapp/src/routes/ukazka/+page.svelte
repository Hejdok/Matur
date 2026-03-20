<script>
    import Button from "../../components/Button.svelte"

    let message = "hi"
    let src = "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1WFAh6.img?w=1200&h=630&m=4&q=81"
    let score = $state(0) // $ reaktivní (runa)

    function increment(){
        score += 3
    }

</script>

<h1>Vše funguje!</h1>

<ul>
    <li>jedna</li>
    <li>dva</li>
    <li>tri</li>
</ul>

<h2>{message.toUpperCase()} rdm</h2>
<img {src} class="image" alt="">
<!-- <img src={src} class="image" alt=""> -->
<p>{score >= 5 ? "GOOD!" : "Neutral"}</p>
<p>Points: {score}</p>
<button onclick={increment}>Click me</button>
<Button/>


<style>
    .image {
        height: 400px;
    }
</style>