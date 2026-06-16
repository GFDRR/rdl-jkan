---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-arbaat-dam-al-ganap-l
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-arbaat-dam-al-ganap-l
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-arbaat-dam-al-ganap-l
dataset_id: rdls_hel-sdn_unosat_preliminaryderivedimpacta_20240902
description: 'UNOSAT code: FL20240826SDN, GDACS ID: 1102854 Status: Affected structures
  detected Further action(s): continue monitoring Summary of findings: Water levels
  have been notably reduced in the Arbaat Dam observed as of 31 August 2024; Flooded
  areas and overflow evidence observed along the waterway in Alganab locality as of
  30 and 31 August 2024; Abunqarah, Kdoweeb, Tobler, Edbye Family Health Units, as
  well as Tedrbai Family Health Centers, appear to be unaffected by floodwaters. Tedrbai,
  Hit Wasat, Tamli, Agoamet Srarah, and Tegilo Family Health Units, as well as Kelkoy
  and Mostehliland Shalhout Family Health Centers, are likely affected by floodwaters..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-arbaat-dam-al-ganap-l]'
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
    description: Health facility structures (Family Health Units and Centers) in Al
      Ganap Locality
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from 30-31
    August 2024 against baseline conditions to detect notable changes in water levels
    at Arbaat Dam and identify flooded areas along waterways. Affected health facility
    structures were identified through visual interpretation of satellite imagery
    and georeferenced in vector format (geodatabase and shapefile).
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-arbaat-dam-al-ganap-l
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected flood impact on health facilities in Al Ganap
      Locality, with assessment of affected and unaffected structures
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
  description: Preliminary satellite-derived impact assessment on health facilities,
    Arbaat Dam, Al Ganap Locality, Red Sea State, Sudan, 2 September 2024 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3941/FL20240826SDN_gdb.zip
  format: Geodatabase
  id: resource_cc04a318
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary satellite-derived impact assessment on health facilities,
    Arbaat Dam, Al Ganap Locality, Red Sea State, Sudan, 2 September 2024 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3941/FL20240826SDN_SHP.zip
  format: null
  id: resource_2d76f74a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sdn_unosat_preliminaryderivedimpacta_20240902
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-02'
temporal_resolution: null
title: Preliminary satellite-derived impact assessment on health facilities, Arbaat
  Dam, Al Ganap Locality, Red Sea State, Sudan, 2 September 2024
version: null
vulnerability: null
---
