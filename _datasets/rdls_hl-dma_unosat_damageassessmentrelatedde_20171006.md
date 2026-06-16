---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-northeastern-part-of-dominica-2702
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-northeastern-part-of-dominica-2702
dataset_id: rdls_hl-dma_unosat_damageassessmentrelatedde_20171006
description: 'This map illustrates potentially damaged structures and buildings in
  the north-western part of Dominica (St. Andrew, St. Joseph & St. David Parishes)
  as detected by satellite image acquired after landfall of the Tropical Cyclone Maria-17
  on 19 September 2017. UNITAR-UNOSAT analysis used a Pleiades image acquired on 23
  September 2017 and a WorldView-3 image acquired on 1 October 2017 as post imagery.
  Within the extent of the analyzed areas, UNITAR-UNOSAT identified in the cloud free
  zones 5,609 potentially damaged structures. Taking into account the pre-building
  footprints provided by Humanitarian OpenStreetMap, this represents about 90 % of
  the total number of structures within the analysed cloud free areas. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-northeastern-part-of-dominica-2702]'
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
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre-event building footprints with post-event
    satellite imagery (Pleiades acquired 23 September 2017 and WorldView-3 acquired
    1 October 2017) to detect structural damage in cloud-free zones of northwestern
    Dominica parishes following Tropical Cyclone Maria-17 landfall on 19 September
    2017, identifying 5,609 potentially damaged structures.
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
- href: https://data.humdata.org/dataset/damage-assessment-related-density-in-the-northeastern-part-of-dominica-2702
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone Maria-17 detected via
      satellite imagery analysis
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Damage Assessment & Related Density in the Northeastern Part of Dominica
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_gdb.zip
  format: Geodatabase
  id: resource_cc1ed9e8
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
  description: Damage Assessment & Related Density in the Northeastern Part of Dominica
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_shp.zip
  format: null
  id: resource_9482b41d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170918DMA_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-dma_unosat_damageassessmentrelatedde_20171006
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
title: Damage Assessment & Related Density in the Northeastern Part of Dominica
version: null
vulnerability: null
---
