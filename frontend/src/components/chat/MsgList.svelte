<script>
    import { fade, scale } from 'svelte/transition'
    import {messageStore} from '../../stores/chat'
    import MsgNode from './MsgNode.svelte';
</script>

{#each $messageStore as msg (msg.id)}
    <div class="flex-grow">
       <MsgNode objAttributes={msg} /> 
    </div>
{/each}