<script>
    import { fade, scale } from 'svelte/transition'
    import { flip } from 'svelte/animate';
    import {messageStore} from '../../stores/chat'
    import MsgNode from './MsgNode.svelte';
</script>

{#each $messageStore as msg (msg.id)}
    <div class="flex-grow" in:fade out:fade|local>
       <MsgNode objAttributes={msg} /> 
    </div>
{/each}