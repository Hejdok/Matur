<script>
    import { shared } from "$lib/shared.svelte";

    let running = false

    function autoclicker(){
        if (running === false){
            running = true
            setInterval(function(){
                shared.score +=1
            }, 1000)
        }
    }



</script>

<button class="btn" onclick={autoclicker}>Autoclicker</button>

<style>
.btn {
    padding: 12px 28px;
    font-size: 16px;
    font-weight: 600;
    color: white;
    background: linear-gradient(135deg, #6a5cff, #8f7bff);
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.25s ease;
    box-shadow: 0 6px 14px rgba(0,0,0,0.15);
}

.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 18px rgba(0,0,0,0.2);
    background: linear-gradient(135deg, #5b4df5, #7d69ff);
    }

.btn:active {
    transform: translateY(1px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
</style>