<template>
    <div id="app">
        <div id='header'>
            <div id='header-logo'>
                <img class='stfc-logo' src='/static/images/stfc_logo.png' alt='STFC-Logo'/>
            </div>
            <div id='header-title'>
                <span id='header-title-text'> 
                    CEPH Performance Tests
                </span>
            </div>
        </div> <!-- Closing Header -->
        <!-- pulls Hello.vue or something -->  <router-view></router-view>
    </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>

#header {
    position: static;
    display: flex;
    height: 120px;
    background-color: #114a8d;
}

#header-logo {
    position: static;
    padding-left: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-right: 10px;
    border-right: 1px solid white;
}

#header-title {
    position: static;
    display: flex;
    color: white;
    font-size: 36px;
    padding-left: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    justify-content: center;
    align-items: center;
}

#header-title-text {
    display: block;
}

</style>
