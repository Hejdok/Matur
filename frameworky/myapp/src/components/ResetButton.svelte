<script>
    import { shared } from "$lib/shared.svelte";
    let { buttonText } = $props()

    function reset(){
        shared.score = 0
    }
    
</script>

<button onclick={reset}>{buttonText}</button>


<style>
    button{
        background-color: rgb(150, 0, 196);
        border: none;
        padding: 10px 20px;
        border-radius: 1000000000px;
    }

    button:hover{
        background-color: rgb(255, 230, 0);
    }

</style>