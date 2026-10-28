// data/test_bio-enzyme.js: logic test for widgets/bio-enzyme.js with a minimal fake W and DOM (run: node data/test_bio-enzyme.js)
const fs = require('fs');
class N { constructor(t){this.tag=t;this.kids=[];this.attrs={};this.style={};this.textContent='';}
  appendChild(c){this.kids.push(c);return c;} setAttribute(k,v){this.attrs[k]=v;} }
function h(tag, props, ...kids){ const n=new N(tag); for(const k in (props||{})){ const v=props[k]; if(k==='text')n.textContent=v; else if(k==='style')Object.assign(n.style,v); else if(k==='html')n.textContent=v; else if(k.slice(0,2)==='on')n[k]=v; else n.attrs[k]=v; }
  kids.forEach(c=>{ if(c!=null) n.appendChild(typeof c==='string'?Object.assign(new N('#t'),{textContent:c}):c); }); return n; }
let reg = null; const sliders=[]; const canv=[]; const ros=[];
global.W = { register:(n,f)=>{reg=f;}, h,
  frame:(el)=>({root:el, body:new N('div')}),
  axes:(ctx,w,hh,v)=>({X:x=>x,Y:y=>y}),
  canvas:(p,o)=>{ const c={redraw:()=>{ o.draw(ctxStub,300,200,colors); o.describe(); c.n++; },n:0}; canv.push(c); p.appendChild(new N('canvas')); return c; },
  sliderNum:(o)=>{ const s={el:new N('slider'),v:o.value,get:()=>s.v,set:v=>{s.v=v;},fire:v=>{s.v=v;o.oninput(v);}}; sliders.push(s); return s; },
  readout:(rows)=>{ const r={el:new N('table'),vals:{},set:(k,v)=>{r.vals[k]=v;}}; ros.push(r); return r; } };
const colors = {ink:'#000',ink2:'#111',ink3:'#222',card:'#fff',sc:'#0a0',red:'#f00',font:'sans'};
const ctxStub = new Proxy({}, { get:(t,k)=> (k in t)?t[k]:(()=>{}), set:(t,k,v)=>{t[k]=v;return true;} });
eval(fs.readFileSync('widgets/bio-enzyme.js','utf8'));
function run(opts){ sliders.length=0; canv.length=0; ros.length=0; const el=new N('div'); const hold={}; reg(el,opts); return el; }
let el = run({mode:'kinetics'});
let ro = ros[ros.length-1];
console.log('kinetics start', JSON.stringify(ro.vals));
if (ro.vals.v!=='80 arbitrary units' || ro.vals.k!=='12 mmol dm⁻³') throw new Error('start state wrong');
sliders[0].fire(60); console.log('Vmax 60', JSON.stringify(ro.vals));
sliders[2].fire(12); console.log('S 12', JSON.stringify(ro.vals));
const body = el; // body is a separate node; find tab buttons through frame stub is not exposed
// temperature
run({mode:'temperature'}); ro=ros[ros.length-1]; sliders[0].fire(41); console.log('T 41', JSON.stringify(ro.vals));
sliders[0].fire(70); console.log('T 70', JSON.stringify(ro.vals));
sliders[0].fire(0); console.log('T 0', JSON.stringify(ro.vals));
run({mode:'ph'}); ro=ros[ros.length-1]; sliders[0].fire(2); console.log('pH 2', JSON.stringify(ro.vals)); sliders[0].fire(11); console.log('pH 11', JSON.stringify(ro.vals));
run({mode:'nonsense', vmax:'abc', km:'-5', s:'999'}); ro=ros[ros.length-1]; console.log('bad attrs', JSON.stringify(ro.vals));
console.log('ok');
