<script>
    import { shared } from "$lib/shared.svelte"
    
    let text = $state("Cheaty")

    let isCorrect = $state(false)

    function cheat(){
        if (text === "scam"){
        shared.score += 100
        isCorrect = true
        }
        else {
        isCorrect = false
        }
        
    }

</script>

<p style="color: {isCorrect ? 'green' : 'black'}" >{text}</p>

<input oninput={cheat} bind:value={text}  type="text">