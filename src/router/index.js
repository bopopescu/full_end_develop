import $ from 'jquery' ;
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import home from '@/components/home'
import App from '@/App'
import NavBottom from '@/components/NavBottom'

Vue.use(Router)

export default new Router({
  routes: [
  {
		path:'/',
		name:'home',
		component:home
	}

  ]
})
