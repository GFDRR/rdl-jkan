---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Kenya Red Cross Society
  url: https://data.humdata.org/dataset/kenya-people-affected-by-elnino
creator:
  affiliation: null
  email: null
  name: Kenya Red Cross Society
  url: https://data.humdata.org/dataset/kenya-people-affected-by-elnino
dataset_id: rdls_lss-ken_krcs_peopleaffectedelnino_2015
description: 'This dataset shows the number of people affected by elnino rains per
  county. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kenya-people-affected-by-elnino]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: "Kenya Red Cross Society compiled direct observational and anecdotal\
    \ data on populations affected by El Ni\xF1o-induced flooding across Kenyan counties\
    \ during the 2015-2016 period. Data was aggregated by county administrative boundaries\
    \ and documented in spreadsheet and shapefile formats to provide spatial impact\
    \ records."
  sources:
  - id: source_1
    license: null
    name: Kenya Red Cross Society
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kenya-people-affected-by-elnino
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Population affected by El Ni\xF1o-induced flooding per county"
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya - People affected by Elnino (Excel)
  download_url: https://data.humdata.org/dataset/f4178cb5-3586-49f8-8bd7-4848235c5b97/resource/041ea6f7-573b-440f-ad2d-0615de108357/download/el_nino_effect.xlsx
  format: null
  id: resource_041ea6f7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: el_nino_effect.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya - People affected by Elnino (Shapefile)
  download_url: http://red_cross_shapefile.zip
  format: null
  id: resource_2e1d5002
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: red_cross_shapefile.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya - People affected by Elnino (Data as of 19th January 2015)
  download_url: https://data.humdata.org/dataset/f4178cb5-3586-49f8-8bd7-4848235c5b97/resource/1357d235-4b53-420d-882a-a241758c8371/download/floods-2015-19th-jan-2016.xlsx
  format: null
  id: resource_1357d235
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FLOODS 2015 -19th jan 2016.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_krcs_peopleaffectedelnino_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-01-19'
  start: '2015-10-01'
temporal_resolution: null
title: Kenya - People affected by Elnino
version: null
vulnerability: null
---
