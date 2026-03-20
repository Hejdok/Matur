<script>
    import Button from "../components/Button.svelte"
    import Timer from "../components/Timer.svelte"
    import ResetButton from "../components/ResetButton.svelte"
    import Upgrade from "../components/Upgrade.svelte"
    import { shared } from "$lib/shared.svelte"
    import Autoclicker from "../components/Autoclicker.svelte"
    import Cheats from "../components/Cheats.svelte"
    import Icon from "../components/Icon.svelte"


    let animScore = $state()
    let animBTN = $state()
    let cheatsVisibility = $state(true)

    $effect(() => {
    if(shared.score > 0) {
        animScore = "anim-score"
        setTimeout(() => animScore = "", 100)
    }


})

</script>

<div><p class={animScore}>{shared.score}</p></div>
<Button buttonText={"click me"}/>
<Button buttonText={"Hello"}/>
<Timer />
<ResetButton buttonText={"Reset"}/>
<Upgrade level={1} --color="rgb(80, 255, 89)"/>
<Upgrade level={2} --color="rgb(160, 255, 89)"/>
<Upgrade level={3} --color="rgb(80, 255, 190)"/>
<Autoclicker />
{#if shared.score > 5}
<button class="cheats-icon" onclick={cheatsVisibility=!cheatsVisibility}>🥷</button>
{/if}
{#if !cheatsVisibility}
<Cheats />
{/if}

<style>
div {
    
    display: flex;
    justify-content: center;
    align-items: center;
}
.anim-score {
    animation: popout 0.1s;
}

.cheats-icon {
    height: 100px;
    position: absolute;
    top: 5%;
    right: 5%;
    width: 100px;
    font-size: 75px;
    border: 0px;
    background-color: white;
}
@keyframes popout {
    50% {
        scale: 3;
    }
    100%{
        scale: 1;
    }
}


</style>