export default function initScrollSection(){function e(e){e.preventDefault();const t=e.currentTarget.getAttribute("href"),o=document.querySelector(t),r=document.querySelector("header"),c=parseFloat(window.getComputedStyle(r).height),n=o.offsetTop-c;window.scrollTo({top:n,behavior:"smooth"})}document.querySelectorAll('[href^="#"]').forEach((t=>{t.addEventListener("click",e)}))}