export default [
  {
    path: '/',
    name: 'landing-page',
    component: require('components/LandingPageView')
  },
  {
    path: '/text-page',
    name: 'text-page',
    component: require('components/TextPageView')
  },
  {
    path: '*',
    redirect: '/'
  }
]
