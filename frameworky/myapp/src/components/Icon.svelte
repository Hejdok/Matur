<script>
    import { shared } from "$lib/shared.svelte";


    function reveal(){
        shared.showCheat = !shared.showCheat
    }
</script>
{#if shared.score > 5}
    <button onclick={reveal}>🎶</button>
{/if}
<style>
    button{
        height: 100px;
        position: absolute;
        top: 5%;
        right: 5%;
        width: 100px;
        font-size: 75px;
        border: 0px;
        background-color: white;
    }
</style>
