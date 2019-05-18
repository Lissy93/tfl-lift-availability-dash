<template>
    <div class="station-lifts">
        <el-table
        :data="liftData"
        style="width: 100%">
            <el-table-column
                prop="name"
                sortable
                label="Name"
                width="240">
            </el-table-column>
            <el-table-column
                prop="status"
                sortable
                label="Status"
                width="180">

                <template slot-scope="scope">
                    <div :class="`color-${makeIconName(scope.row.status)}`">
                        <i :class="`el-icon-${makeIconName(scope.row.status)}`"></i>
                        <span>{{ makeStatusName(scope.row.status)}}</span>
                    </div>
                </template>

            </el-table-column>
            <el-table-column
                prop="statusDescription"
                label="Details">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
  name: 'StationStatusTable',
  props: {
    liftData: Array,
  },
  methods: {
    makeStatusName(statusCode) {
        switch (statusCode) {
            case 0: return 'Critical';
            case 1: return 'Restricted';
            case 2: return 'Operational'
            default: return 'Unknown';
        }
      },
    makeIconName(statusCode) {
        switch (statusCode) {
            case 0: return 'error';
            case 1: return 'warning';
            case 2: return 'success'
            default: return 'question';
        }
      }
  }
}
</script>

<style scoped lang="scss">

    /deep/ .el-icon-success, 
    .el-icon-warning,
    .el-icon-error,
    .el-icon-question {
        font-size: 1.5em;
        margin: 5px;
    }

    /deep/ .el-table__row td {
        padding: 8px 0;
    }

    /deep/ .el-table_1_column_1 {
        font-weight: bold;
    }

    .color-success {
        color: #67C23A;
    }
    .color-warning {
        color: #E6A23C;
    }
    .color-error {
        color: #F56C6C;
    }
    .color-question {
        color: #909399;
    }

</style>
