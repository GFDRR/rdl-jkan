---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    url: https://data.humdata.org/dataset/tasa-de-afectados-por-desastres-por-cada-100mil-habitantes-entre-2019-y-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Departamento Nacional de Estad\xEDstica (DANE)"
    url: https://data.humdata.org/dataset/tasa-de-afectados-por-desastres-por-cada-100mil-habitantes-entre-2019-y-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/tasa-de-afectados-por-desastres-por-cada-100mil-habitantes-entre-2019-y-2020
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/tasa-de-afectados-por-desastres-por-cada-100mil-habitantes-entre-2019-y-2020
dataset_id: rdls_lss-col_immap_tasadeafectadospordesastr
description: "Esta base de datos contiene la tasa de personas afectadas por desastres\
  \ por cada 100.000 habitantes en cada municipio de Colombia entre 2019 y 2020. La\
  \ metodolog\xEDa utilizada para el c\xE1lculo de este indicador fue tomada y adaptada\
  \ del Plan Nacional de Gesti\xF3n del Riesgo de Desastres de la UNGRD (Unidad Nacional\
  \ de Gesti\xF3n del Riesgo de Desastres). La tasa se deriva de dividir el promedio\
  \ del n\xFAmero de personas afectadas por desastres en un periodo de tiempo entre\
  \ el promedio de poblaci\xF3n para dicho periodo, y posteriormente, multiplicar\
  \ el resultado por 100.000. Las fuentes de informaci\xF3n para este c\xE1lculo fueron\
  \ los registros de la UNGRD y las proyecciones de poblaci\xF3n del DANE.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/tasa-de-afectados-por-desastres-por-cada-100mil-habitantes-entre-2019-y-2020]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Disaster-affected population counts from UNGRD registry were aggregated
    by municipality and time period (2019-2020), then normalized by corresponding
    municipal population estimates from DANE to produce standardized rates per 100,000
    inhabitants following UNGRD methodology.
  sources:
  - id: source_1
    license: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Departamento Nacional de Estad\xEDstica (DANE)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tasa-de-afectados-por-desastres-por-cada-100mil-habitantes-entre-2019-y-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Rate of population affected by disasters per 100,000 inhabitants
      at municipal level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Rate of population affected by disasters per 100,000 inhabitants
      at municipal level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Rate of population affected by disasters per 100,000 inhabitants
      at municipal level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Rate of population affected by disasters per 100,000 inhabitants
      at municipal level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - Tasa de Afectados por Desastres por cada 100mil habitantes\
    \ entre 2019 y 2020 (Base de datos de poblaci\xF3n afectada por municipio en formato\
    \ xlsx.)"
  download_url: https://data.humdata.org/dataset/91d0f12e-110f-4099-95a6-75d9be3bd716/resource/40ef29d7-8097-4261-be42-186705cb7473/download/tasa_afectados_desastres_2019_2020.xlsx
  format: null
  id: resource_40ef29d7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tasa_Afectados_Desastres_2019_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - Tasa de Afectados por Desastres por cada 100mil habitantes\
    \ entre 2019 y 2020 (Base de datos de poblaci\xF3n afectada por municipio en formato\
    \ csv.)"
  download_url: https://data.humdata.org/dataset/91d0f12e-110f-4099-95a6-75d9be3bd716/resource/cb7b66c4-0052-4cc7-a59f-30ec32cf74de/download/tasa_afectados_desastres_2019_2020.csv
  format: null
  id: resource_cb7b66c4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tasa_Afectados_Desastres_2019_2020.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Tasa de Afectados por Desastres por cada 100mil habitantes
    entre 2019 y 2020 (Diccionario de variables.)
  download_url: https://data.humdata.org/dataset/91d0f12e-110f-4099-95a6-75d9be3bd716/resource/969983eb-3267-4b08-b91e-f113759ee547/download/diccionario_variables_tasa_afectados.xlsx
  format: null
  id: resource_969983eb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Diccionario_Variables_Tasa_Afectados.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_immap_tasadeafectadospordesastr
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Colombia - Tasa de Afectados por Desastres por cada 100mil habitantes entre
  2019 y 2020
version: null
vulnerability: null
---
