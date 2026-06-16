---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus
    url: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-central-southern-parts-of-dominica-2704
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-central-southern-parts-of-dominica-2704
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-central-southern-parts-of-dominica-2704
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-central-southern-parts-of-dominica-2704
dataset_id: rdls_el-dma_unosat_damageassessmentrelatedde_20171006
description: 'This map illustrates potentially damaged structures and buildings in
  the Central and Southern parts of Dominica (St. Patrick, St. Mak, St. George, St.
  Luke, St. David & St. Paul Parishes) as detected by satellite image acquired after
  landfall of the Tropical Cyclone Maria-17 on 19 September 2017. The UNITAR-UNOSAT
  analysis combined with Copernicus analysis, identified 12,873 potentially damaged
  structures in this zone. Taking into account the pre-building footprints provided
  by Humanitarian OpenStreetMap, this represents about 70 % of the total number of
  structures within the analyzed areas. Please note that some areas could not be analyzed
  due to the cloud cover. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-central-southern-parts-of-dominica-2704]'
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
    description: Building footprints and structures in Central and Southern Dominica
      parishes
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
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired before and after
    Tropical Cyclone Maria's landfall on 19 September 2017 to detect structural changes.
    Copernicus analysis contributed to the damage detection methodology. Pre-event
    building footprints from Humanitarian OpenStreetMap were used as a baseline to
    calculate that 12,873 potentially damaged structures represented approximately
    70% of total structures in the analyzed parishes.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Copernicus
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-central-southern-parts-of-dominica-2704
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone Maria detected via satellite
      imagery analysis
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
  description: Damage Assessment & Related Density in the Central & Southern Parts
    of Dominica (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_gdb.zip
  format: Geodatabase
  id: resource_2b1642f8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170918DMA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment & Related Density in the Central & Southern Parts
    of Dominica (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_shp.zip
  format: null
  id: resource_fed434e4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170918DMA_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-dma_unosat_damageassessmentrelatedde_20171006
spatial:
  bbox: null
  centroid: null
  countries:
  - DMA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-06'
temporal_resolution: null
title: Damage Assessment & Related Density in the Central & Southern Parts of Dominica
version: null
vulnerability: null
---
