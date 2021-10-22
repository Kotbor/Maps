<template>
<div>
  <v-row>
    
     <v-col cols="12" sm="12" md="4">
        
      </v-col>
     
  </v-row>
    <v-row cols="8" align="center" justify="center">
  <v-data-table 
    :headers="headers"
    :items="users"
    :search="search"
    class="elevation-2"
  >
    <template v-slot:top>
      
      <v-toolbar 
        text
      >
      <v-col cols="6" md="3" sm="3">
        <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Поиск"
        single-line
        hide-details
      ></v-text-field>
      </v-col>
        <v-spacer></v-spacer>
        
        <v-dialog
          v-model="dialog"
          max-width="800px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="#4caf50"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Новая запись
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="Имя"
                    ></v-text-field>
                  </v-col>
               
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.email"
                      label="E-mail"
                    ></v-text-field>
                  </v-col>
                  
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.password"
                      label="Пароль"
                    ></v-text-field>
                    
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="red darken-1"
                text
                @click="close"
              >
                Отмена
              </v-btn>
              <v-btn
                color="green darken-1"
                text
                @click="save"
              >
                Сохранить
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5 justify-center">Точно удалить запись ?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Отмена</v-btn>
              <v-btn color="red darken-1" text @click="deleteItemConfirm">Удаляем</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <!--eslint-disable-next-line-->
    <template v-slot:item.actions="{ item }">
      <v-icon
        
        color="orange"
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      
      <v-icon
        color="red"
        
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      Нет данных
    </template>
  </v-data-table>
  </v-row>
</div>
</template>

<script>
  import qs from 'qs';
  export default {
    data: () => ({

      search: '',
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'Имя',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'E-mail', value: 'email', sortable: false},
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      users: [],
      editedIndex: -1,
      editedItem:{
            name: '',
            email: "",
            password: ""
          },
      defaultItem: {
            name: '',
            email: "",
            password: ""
      },
     
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Новая запись' : 'Изменить запись'
      }
      
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        this.axios.get('http://localhost:8000/api/get_users/').then((response)=>{
            this.users = response.data
        })
        

      },

      editItem (item) {
        this.editedIndex = this.users.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.users.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.desserts.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.users[this.editedIndex], this.editedItem)
        } else {
          console.log(qs.stringify(this.editedItem))
          this.axios({
          method: 'post',
          url:'http://192.168.10.5:8000/api/add_user/',
          headers: { 'content-type': 'application/x-www-form-urlencoded' },
          data: qs.stringify(this.editedItem),
        }).then(() =>{
            this.users.push(this.editedItem)
        }).catch(()=> {this.Error=true})
          
          
        }
        this.close()
      },
    },
  }
</script>
  