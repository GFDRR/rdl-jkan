---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-north-santo-antao-island-cabo-verde
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-north-santo-antao-island-cabo-verde
dataset_id: rdls_lss-cpv_unosat_preliminaryderivedfloodim_20250818
description: "UNOSAT code: FL20250812CPV Status: No major damage was observed Further\
  \ action(s): Continue monitoring Summary of findings: No major damage was observed\
  \ in Ponta do Sol Town, Cruzinha Village, and Ribeira da Cruz Village in northern\
  \ Santo Ant\xE3o Island as of 16 August 2025. Possible flood evidence was observed\
  \ along the waterways in Ribeira Grande Town and Coculi Town in northern Santo Ant\xE3\
  o Island as of 16 August 2025.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-north-santo-antao-island-cabo-verde]"
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
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed and compared satellite imagery acquired on\
    \ 16 August 2025 with reference imagery to identify flood-related changes and\
    \ damage in northern Santo Ant\xE3o Island. Visual interpretation of satellite\
    \ data was used to map areas with flood evidence and assess damage status in affected\
    \ towns and villages."
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-north-santo-antao-island-cabo-verde
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: "Post-event satellite-derived assessment of building damage from\
      \ flooding in Santo Ant\xE3o Island"
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
  description: Preliminary Satellite-derived Flood Impact Assessment, North Santo
    Antao Island, Cabo Verde (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4173/FL20250812CPV_GDB.zip
  format: Geodatabase
  id: resource_a4616a26
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary Satellite-derived Flood Impact Assessment, North Santo
    Antao Island, Cabo Verde (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4173/FL20250812CPV_SHP.zip
  format: null
  id: resource_9d49ec6c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cpv_unosat_preliminaryderivedfloodim_20250818
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-08-18'
temporal_resolution: null
title: Preliminary Satellite-derived Flood Impact Assessment, North Santo Antao Island,
  Cabo Verde
version: null
vulnerability: null
---
