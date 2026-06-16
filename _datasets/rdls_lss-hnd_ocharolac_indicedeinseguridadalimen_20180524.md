---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad T\xE9cnica de Seguridad Alimentaria y Nutricional (UTSAN)"
    url: https://data.humdata.org/dataset/honduras-indice-de-inseguridad-alimentaria-2012
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Programa Mundial de Alimentos (PMA)
    url: https://data.humdata.org/dataset/honduras-indice-de-inseguridad-alimentaria-2012
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-indice-de-inseguridad-alimentaria-2012
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-indice-de-inseguridad-alimentaria-2012
dataset_id: rdls_lss-hnd_ocharolac_indicedeinseguridadalimen_20180524
description: "El ICA se basa en el an\xE1lisis de las tendencias hist\xF3ricas de\
  \ inseguridad alimentaria y los principales riesgos naturales, incorporara el nivel\
  \ de fragilidad econ\xF3mica, la degradaci\xF3n de la tierra y los medios de vida.\
  \ Se clasifica en 5 categor\xEDas, 1 representa una mayor recurrencia de inseguridad\
  \ alimentaria, y 5 una menor recurrencia.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras-indice-de-inseguridad-alimentaria-2012]"
details: "* [INFORM Honduras.](http://www.inform-index.org/Subnational/Honduras) *\
  \ Dimensi\xF3n: Vulnerabilidad * Categor\xEDa: Grupos Vulnerables * Componente:\
  \ Otros Grupos Vulnerables"
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The Food Insecurity Index (ICA) integrates historical trends of food
    insecurity with natural hazard exposure, economic fragility, land degradation,
    and livelihood vulnerability. Data from UTSAN and WFP were analyzed to classify
    municipalities into 5 categories (1=highest recurrence of food insecurity, 5=lowest),
    producing a composite vulnerability and impact index at the national level.
  sources:
  - id: source_1
    license: null
    name: "Unidad T\xE9cnica de Seguridad Alimentaria y Nutricional (UTSAN)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Programa Mundial de Alimentos (PMA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-indice-de-inseguridad-alimentaria-2012
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity classification incorporating drought and natural
      hazard risks affecting agricultural livelihoods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: "Honduras \xCDndice de Inseguridad Alimentaria 2012 (\xCDndice de Inseguridad\
    \ Alimentaria - An\xE1lisis Integrado de Contexto (ICA) 2012.)"
  download_url: https://data.humdata.org/dataset/4267faa0-3ca2-4cf1-993a-85bb04cbc5aa/resource/53b50091-1327-4c47-9ae3-d0e448e19baf/download/12-vu.gv.ogv.iia-indice-de-seguridad-alimentaria.xlsx
  format: null
  id: resource_53b50091
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "12-VU.GV.OGV.IIA - \xCDndice de Seguridad Alimentaria.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_ocharolac_indicedeinseguridadalimen_20180524
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-24'
temporal_resolution: null
title: "Honduras \xCDndice de Inseguridad Alimentaria 2012"
version: null
vulnerability: null
---
