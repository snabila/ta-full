import { writable } from 'svelte/store';

export const pageName = writable('Dashboard');
export let storeFields = writable([]);
