---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-ringerike-municipality-viken-county-norway-as-of-12-august-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-ringerike-municipality-viken-county-norway-as-of-12-august-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-ringerike-municipality-viken-county-norway-as-of-12-august-2023
dataset_id: rdls_hl-nor_unosat_detectedwaterextentoverri_20230814
description: "UNOSAT code FL20230811NOR This map illustrates satellite-detected water\
  \ extent as observed from a Pl\xE9iades imagery acquired on the 12 August 2023 at\
  \ 13:31 local time.Within the analysed area of about 16,000 ha, a total of about\
  \ 255 ha of lands appear to be affected with flood waters. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extent-over-ringerike-municipality-viken-county-norway-as-of-12-august-2023]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "Pl\xE9iades satellite imagery acquired on 12 August 2023 was analyzed\
    \ by UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ to detect changes in water extent. The resulting water polygon layer represents\
    \ observed flood inundation covering approximately 255 hectares within a 16,000\
    \ hectare study area in Ringerike Municipality."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-ringerike-municipality-viken-county-norway-as-of-12-august-2023
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct land area affected by flood waters as detected from satellite
      imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Satellite detected water extent over Ringerike Municipality, Viken
    County, Norway as of 12 August 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3658/FL20230811NOR_gdb.zip
  format: Geodatabase
  id: resource_ffb01e7c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230811NOR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Ringerike Municipality, Viken
    County, Norway as of 12 August 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3658/FL20230811NOR_SHP.zip
  format: null
  id: resource_4a1b8257
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230811NOR_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-nor_unosat_detectedwaterextentoverri_20230814
spatial:
  bbox: null
  centroid: null
  countries:
  - NOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-14'
temporal_resolution: null
title: Satellite detected water extent over Ringerike Municipality, Viken County,
  Norway as of 12 August 2023
version: null
vulnerability: null
---
