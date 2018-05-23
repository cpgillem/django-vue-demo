import axios from 'axios';
import baseUrl from './baseUrl';

/* This module creates an instance of axios with the correct defaults. */
export default axios.create({
    baseURL: baseUrl,
});