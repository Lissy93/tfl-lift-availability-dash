<template>
    <div class="station-lifts">
        <el-table
        v-if="liftData.length > 0"
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

        <div class="tile-footer">
            <el-tooltip effect="dark" content="Save station to favourites" placement="top">
                <el-button plain icon="el-icon-star-off" circle></el-button>
            </el-tooltip>

            <el-tooltip 
                effect="dark" placement="top"
                content="Send SMS alerts when lifts in this station  statuschange">
                <el-button
                    type="primary"
                    plain
                    class="alert-button"
                    @click="dialogVisible = true"
                >
                    Create Alert
                    <i class="el-icon-message-solid icon" />
                </el-button>
            </el-tooltip>
        </div>

       

        <el-dialog
            :visible.sync="dialogVisible"
            width="50%"
        >
            <NotificationForm />
        </el-dialog>

    </div>
</template>

<script>
import NotificationForm from '@/components/NotificationForm.vue';

export default {
  name: 'StationStatusTable',
  props: {
    liftData: Array,
  },
  components: {
      NotificationForm,
  },
  data() {
      return {
        dialogVisible: false
      };
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

.tile-footer {
    .el-button {
                align-self: flex-start;
                margin: 15px 15px 0;
            }
}

    .station-lifts {
        align-items: flex-end;
    }

    .alert-button {
        width: 15em;
        margin: 15px 10px -10px 0;
        .icon {
            margin: 0 5px;
            font-size: 1.2em;
        }
    }

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

    /deep/ .el-dialog__body,
    el-dialog__header {
        padding: 10px;
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
