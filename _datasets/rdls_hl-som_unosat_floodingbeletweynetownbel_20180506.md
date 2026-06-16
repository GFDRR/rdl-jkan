---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/somalia-flooding-belet-weyne-town-belet-weyne-district-hiiran-region
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/somalia-flooding-belet-weyne-town-belet-weyne-district-hiiran-region
dataset_id: rdls_hl-som_unosat_floodingbeletweynetownbel_20180506
description: 'UNOSAT produced satellite-detected flood water extent and IDP distribtuion
  within the town of Belet Weyne in Belet Weyne District,Hiiran Region, Somalia. The
  analysis was conducted analyzing GeoEye-1 & WorldView-3 images acquired on the 30
  April & 1 May 2018. As observed from the satellite image, the town of Belet Weyne
  is completely affected by the floods. Around 70% of the extension of the town is
  totally inundated, being the districts of Bulahabley, Bundaweyn, Dhagahjebis, Hilac,
  Hindab and Lamagalay Regional Military Based, Radar and Kutimbo completely submerged
  in water. The flood waters inside areas of partially flooded districts are receding.
  More than 110 IDP sites are located inside the town, and 50% of them are inside
  areas completly flooded. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-flooding-belet-weyne-town-belet-weyne-district-hiiran-region]'
details: This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR UNOSAT.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analyzed multispectral satellite imagery (GeoEye-1 and WorldView-3)
    acquired on 30 April and 1 May 2018 to delineate flood water extent polygons in
    Belet Weyne town, with confidence levels and field validation. IDP distribution
    was analyzed concurrently to assess population displacement impacts from the observed
    inundation.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-flooding-belet-weyne-town-belet-weyne-district-hiiran-region
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: IDP distribution and displacement from flooding in Belet Weyne town
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
        metric: displaced
        modelling: observed
        type: direct
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
  description: Somalia flooding Belet Weyne Town, Belet Weyne District, Hiiran Region
    (Satellite detected water & IDP distribution over Belet Weyne Town)
  download_url: https://data.humdata.org/dataset/6bcd7188-24a8-4b2f-8d1e-fc30f5144589/resource/48bc87d0-7e6c-4b33-8414-6e936f06520c/download/rs20180506_ge20180430_beletweyne_flood_analysis.zip
  format: null
  id: resource_48bc87d0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RS20180506_GE20180430_beletweyne_Flood_Analysis.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia flooding Belet Weyne Town, Belet Weyne District, Hiiran Region
    (IDP distribution over Belet Weyne Town)
  download_url: https://data.humdata.org/dataset/6bcd7188-24a8-4b2f-8d1e-fc30f5144589/resource/8a61c22d-57cb-429e-9d54-599f1ab2b91c/download/idp_analysis_belet_weyne_flood.xlsx
  format: null
  id: resource_8a61c22d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP_analysis_Belet_Weyne_Flood.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_unosat_floodingbeletweynetownbel_20180506
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-06'
temporal_resolution: null
title: Somalia flooding Belet Weyne Town, Belet Weyne District, Hiiran Region
version: null
vulnerability: null
---
