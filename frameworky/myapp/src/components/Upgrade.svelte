<script>
    import { shared } from "$lib/shared.svelte";

    let { level } = $props()
    let upgradeClikced = $state(false)
    
    function upgrade(){
        if (level === 1)
        shared.multi = 2
        else if (level === 2)
        shared.multi = 5
        else if (level === 3)
        shared.multi = 10


        upgradeClikced = true
    }


</script>
<div>
{#if upgradeClikced}
<p>Upgraded</p>
{:else}
<p>Upgrade clicker</p>
{/if}

<button id="btn1" onclick={upgrade}>Upgrade</button>

</div>
<style>
    button{
        background-color: var(--color);
        border: none;
        padding: 10px 20px;
        border-radius: 1000000000px;
    }

    button:hover{
        background-color: rgb(42, 85, 165);
    }

    div{
        display: inline-block;
        width: 300px;
        margin: 40px auto;

        font-family: "Comic Sans MS", cursive;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        padding: 40px;

        color: yellow;
        text-shadow:
            0 0 5px red,
            0 0 10px red,
            0 0 20px orange,
            0 0 30px magenta;

        background: linear-gradient(
            45deg,
            red,
            orange,
            yellow,
            lime,
            cyan,
            blue,
            magenta,
            red
        );

        background-size: 200% 200%;

        border: 10px dashed gold;
        border-radius: 30px;

        box-shadow:
            0 0 20px red,
            0 0 40px yellow,
            0 0 60px magenta,
            inset 0 0 30px white;

        animation:
            rainbowMove 4s linear infinite,
            blink 0.8s infinite,
            rotateWobble 3s ease-in-out infinite;
    }

    @keyframes rainbowMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }

    @keyframes rotateWobble {
        0% { transform: rotate(-2deg) scale(1); }
        50% { transform: rotate(2deg) scale(1.05); }
        100% { transform: rotate(-2deg) scale(1); }
    }

    #btn1 {
        font-family: "Comic Sans MS", cursive;
        font-size: 20px;
        font-weight: bold;

        padding: 12px 25px;

        color: red;
        background: var(--color);

        border: 5px dotted red;
        border-radius: 15px;

        text-shadow:
            1px 1px 0 white,
            0 0 5px yellow,
            0 0 10px orange;

        box-shadow:
            0 0 10px red,
            0 0 20px yellow,
            inset 0 0 10px white;

        cursor: pointer;
    }

</style>