<template>
    <el-alert
      show-icon
      title="Live Data Warning"
      description=
        "This site no longer uses live data, which we lost access to after the hackathon.
        Lift data is now just hard-coded for demo purposes, so do not use it for planning a journey!"
      type="info">
    </el-alert>
</template>

<script>
export default {
  name: 'DemoBanner',
}
</script>


