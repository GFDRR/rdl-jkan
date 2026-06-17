---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Pl\xE9iades satellite imagery"
    url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-lima-kaum-rambatanm-and-pariangan-districts-indonesia-as-of-17-ma
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-lima-kaum-rambatanm-and-pariangan-districts-indonesia-as-of-17-ma
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-lima-kaum-rambatanm-and-pariangan-districts-indonesia-as-of-17-ma
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-lima-kaum-rambatanm-and-pariangan-districts-indonesia-as-of-17-ma
dataset_id: rdls_hel-idn_unosat_mudslidelaharimpactlimaka_20240520
description: "UNOSAT code: LS20240512IDN, GDACS ID: 1102617 This map illustrates satellite-detected\
  \ mudslide / lahar in Lima Kaum, Rambatanm and Pariangan Districts, Tanah Datar\
  \ Metropolitan, Sumatera Barat Province, Indonesia, as observed from a Pl\xE9iades\
  \ image acquired on 17 May 2024. Within the analyzed area of about 50 km\xB2, about\
  \ 1.3 km\xB2 mudslide / lahar extent was observed. Based on Worldpop population\
  \ data and the maximal mudslide / lahar extent ~1,200 people are potentially exposed\
  \ or living close to the affected areas. Furthermore, within the analyzed area,\
  \ 240 buildings are identified as affected by the floods (1% from the total structures\
  \ in the analysed area), along with about 2 km of roads, as of 17 May 2024 This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/mudslide-lahar-impact-in-lima-kaum-rambatanm-and-pariangan-districts-indonesia-as-of-17-ma]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population potentially exposed or living close to mudslide/lahar
      affected areas based on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Building stock identified within the analyzed area
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Pl\xE9iades satellite imagery acquired on\
    \ 17 May 2024 to detect and delineate mudslide/lahar extent in the study area.\
    \ Population exposure was estimated by intersecting the mapped mudslide/lahar\
    \ extent with WorldPop gridded population data, and building counts were identified\
    \ through manual feature extraction from satellite imagery."
  sources:
  - id: source_1
    license: null
    name: "Pl\xE9iades satellite imagery"
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mudslide-lahar-impact-in-lima-kaum-rambatanm-and-pariangan-districts-indonesia-as-of-17-ma
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to mudslide/lahar event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings identified within mudslide/lahar affected extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mudslide / Lahar impact in Lima Kaum, Rambatanm and Pariangan Districts,
    Indonesia, as of 17 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3850/LS20240512IDN.gdb.zip
  format: Geodatabase
  id: resource_632ace86
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240512IDN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mudslide / Lahar impact in Lima Kaum, Rambatanm and Pariangan Districts,
    Indonesia, as of 17 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3850/LS20240512IDN_SHP.zip
  format: null
  id: resource_55eadf5d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240512IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_mudslidelaharimpactlimaka_20240520
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-20'
temporal_resolution: null
title: Mudslide / Lahar impact in Lima Kaum, Rambatanm and Pariangan Districts, Indonesia,
  as of 17 May 2024
version: null
vulnerability: null
---
