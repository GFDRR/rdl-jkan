---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-imias-area-guantanamo-province-cuba
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-imias-area-guantanamo-province-cuba
dataset_id: rdls_lss-cub_unosat_damageassessmentimiasarea_20161012
description: 'This map illustrates potential satellite-detected damaged structures
  in Imias and the surrounding area in Guantanamo Province, Cuba. The UNITAR-UNOSAT
  analysis used a Pleiades satellite image, acquired on the 10 October 2016, and identified
  552 damaged structures within the map extent and 603 damaged structures in the covered
  area. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-in-imias-area-guantanamo-province-cuba]'
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
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 10
    October 2016 and compared it with reference imagery to identify structural damage.
    Damaged structures were manually delineated and counted, yielding 552 structures
    within the map extent and 603 in the covered area. This preliminary assessment
    was not field-validated at the time of publication.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-imias-area-guantanamo-province-cuba
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone assessed via satellite
      imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Damage Assessment in Imias area,Guantanamo province, Cuba (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB.gdb.zip
  format: Geodatabase
  id: resource_ed05e88a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161005CUB.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Imias area,Guantanamo province, Cuba (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB_shp.zip
  format: null
  id: resource_063869d0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161005CUB_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cub_unosat_damageassessmentimiasarea_20161012
spatial:
  bbox: null
  centroid: null
  countries:
  - CUB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-12'
temporal_resolution: null
title: Damage Assessment in Imias area,Guantanamo province, Cuba
version: null
vulnerability: null
---
