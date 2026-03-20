<script>
    import { shared } from "$lib/shared.svelte";
    let { buttonText } = $props()

    function increment(){
        shared.score = shared.score + shared.multi
    }
</script>

<button onclick={increment}>{buttonText}</button>

<style>
    button{
        background-color: coral;
        border: none;
        padding: 10px 20px;
        border-radius: 1000000000px;
        transition: 0.2 ease;
    }

    button:hover{
        background-color: brown;
        
    }

    button:active{
        transform: scale(0.8);
    }


</style>