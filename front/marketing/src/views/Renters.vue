<template>
<div>
  <v-row>
    
     <v-col cols="12" sm="12" md="4">
        
      </v-col>
     
  </v-row>
  <v-row>
      <v-col cols="12" sm="12" md="12">
      <v-card
    text
    color="transparent elevation-2"

  >
    <v-subheader>Требуемый метраж</v-subheader>

    <v-card-text>
      <v-row>
        <v-col class="px-4">
          <v-range-slider
          
            v-model="range"
            :max="max"
            :min="min"
            hide-details
            class="align-center pt-3"
          >
            <template v-slot:prepend>
              <v-text-field
                :value="range[0]"
                class="mt-0 pt-0"
                hide-details
                single-line
                type="number"
                style="width: 60px"
                @change="$set(range, 0, $event)"
              ></v-text-field>
            </template>
            <template v-slot:append>
              <v-text-field
                :value="range[1]"
                class="mt-0 pt-0"
                hide-details
                single-line
                type="number"
                style="width: 60px"
                @change="$set(range, 1, $event)"
              ></v-text-field>
            </template>
          </v-range-slider>
        </v-col>
         <v-col
                    cols="12"
                    sm="12"
                    md="2"
                  >
                <v-select
                    clearable=true 
                    label="Вид деятельности" 
                    :items="selectItems"
                    v-model="activityType"
                  ></v-select>
      </v-col>
      </v-row>
    </v-card-text>
      </v-card>
      </v-col>
  </v-row>
  <v-data-table
    :headers="headers"
    :items="filteredItems"
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
                      v-model="editedItem.phone"
                      label="Телефон"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.e_mail"
                      label="E-mail"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="8"
                  >
                    <v-select
                       :items="selectItems"
                       v-model="editedItem.activity_kind"
                        label="Вид деятельности"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.meters_required"
                      label="Требуемый метраж"
                    ></v-text-field>
                    
                  </v-col>
                  <v-col
                    cols="12"
                    sm="12"
                    md="12"
                  >
                    <v-text-field
                      v-model="editedItem.comments"
                      label="Особые требования"
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
</div>
</template>

<script>
  
  export default {
    data: () => ({
      min: 5,
      max: 100,
      range: [15, 70],
      activityType: null,
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
        { text: 'Телефон', value: 'phone', sortable: false},
        { text: 'E-mail', value: 'e_mail', sortable: false},
        { text: 'Вид деятельности', value: 'activity_kind' },
        { text: 'Требуемый метраж', value: 'meters_required', align:"center" },
        { text: 'Особые требования', value: 'comments', sortable: false },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      desserts: [],
      editedIndex: -1,
      editedItem:{
            name: '',
            phone: "",
            e_mail: "",
            activity_kind: "",
            meters_required: 0,
            comments: ""
          },
      defaultItem: {
            name: '',
            phone: "",
            e_mail: "",
            activity_kind: "",
            meters_required: 0,
            comments: ""
      },
      menu: [
        { icon: "home", title: "Пользователи", link:"users" },
        { icon: "info", title: "Адреса", link:"addresses" },
        { icon: "warning", title: "Виды деятельности", link:"activity" }
      ],
      selectItems:
      [
        "Автосервис","Общепит","Мойка","Продажи","Производство"
      ]
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Новая запись' : 'Изменить запись'
      },
      filteredItems() {
      var items = this.desserts.filter((i) => {
        return !this.activityType || (i.activity_kind === this.activityType);
      })
      var filteredBySize = items.filter((i) =>{ 
        return ((i.meters_required<=this.range[1]) && (this.range[0]<=i.meters_required))
      })

      return filteredBySize
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
        this.desserts =[
  {
    "_id": "614c5ea99c9681a409265aac",
    "name": "Анна",
    "phone": "+7(812)873-63-37",
    "e_mail": "123@45.ru",
    "activity_kind": "Мойка",
    "meters_required": 44,
    "comments": "Спальный район"
  },
  {
    "_id": "614c5ea907fa348dfe207233",
    "name": "Сергей Александрович",
    "phone": "+7(812)697-98-14",
    "e_mail": "123@45.ru",
    "activity_kind": "Общепит",
    "meters_required": 86,
    "comments": "Рядом с метро"
  },
  {
    "_id": "614c5ea946a0270553c5bccb",
    "name": "Геннадий Петрович",
    "phone": "+7(812)928-23-23",
    "e_mail": "123@45.ru",
    "activity_kind": "Производство",
    "meters_required": 31,
    "comments": "Рядом с метро"
  },
  {
    "_id": "614c5ea913bd0311d2896a5a",
    "name": "Анна",
    "phone": "+7(812)359-45-90",
    "e_mail": "123@45.ru",
    "activity_kind": "Мойка",
    "meters_required": 66,
    "comments": "Спальный район"
  },
  {
    "_id": "614c5ea9afecec890e3a9d89",
    "name": "Татьяна Евгеньевна",
    "phone": "+7(812)372-33-42",
    "e_mail": "123@45.ru",
    "activity_kind": "Автосервис",
    "meters_required": 86,
    "comments": "Рядом с метро"
  },
  {
    "_id": "614c5ea981147a4bb4116624",
    "name": "Добрыня Никитич",
    "phone": "+7(812)981-01-23",
    "e_mail": "123@45.ru",
    "activity_kind": "Автосервис",
    "meters_required": 22,
    "comments": "Спальный район"
  },
  {
    "_id": "614c5ea9f521378c51e12bc7",
    "name": "Добрыня Никитич",
    "phone": "+7(812)493-61-11",
    "e_mail": "123@45.ru",
    "activity_kind": "Автосервис",
    "meters_required": 100,
    "comments": "Электричество и вода"
  },
  {
    "_id": "614c5ea9e636a6062445caaa",
    "name": "Владимир",
    "phone": "+7(812)721-19-42",
    "e_mail": "123@45.ru",
    "activity_kind": "Автосервис",
    "meters_required": 25,
    "comments": "На окраине"
  },
  {
    "_id": "614c5ea9ea17f15011575887",
    "name": "Анна",
    "phone": "+7(812)409-65-97",
    "e_mail": "123@45.ru",
    "activity_kind": "Общепит",
    "meters_required": 65,
    "comments": "Рядом с метро"
  },
  {
    "_id": "614c5ea97fb76d5e09d0e4dd",
    "name": "Добрыня Никитич",
    "phone": "+7(812)416-18-51",
    "e_mail": "123@45.ru",
    "activity_kind": "Продажи",
    "meters_required": 93,
    "comments": "На окраине"
  },
  {
    "_id": "614c5ea9b9f601d25c6bfb50",
    "name": "Татьяна Евгеньевна",
    "phone": "+7(812)486-80-61",
    "e_mail": "123@45.ru",
    "activity_kind": "Мойка",
    "meters_required": 32,
    "comments": "Спальный район"
  },
  {
    "_id": "614c5ea9c829a2af0b87b9fb",
    "name": "Геннадий Петрович",
    "phone": "+7(812)791-50-43",
    "e_mail": "123@45.ru",
    "activity_kind": "Общепит",
    "meters_required": 18,
    "comments": "На окраине"
  }
]

      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
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
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
          
        }
        this.close()
      },
    },
  }
</script>
  