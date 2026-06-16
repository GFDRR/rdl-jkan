---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-tiburon-town-and-surroundings
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-tiburon-town-and-surroundings
dataset_id: rdls_lss-hti_unosat_damageassessmenttiburonto_20161027
description: 'This map illustrates satellite-detected potentially damaged buildings
  in Tiburon town, Sud department, Haiti. The UNITAR-UNOSAT analysis used a WorldView-2
  satellite image acquired on the 17 July 2016 as a pre-image and a Worldview- 2 satellite
  image acquired on the 17 October 2016 as a post-image. The UNITAR-UNOSAT analysis
  identified 648 potentially damaged structures within the map extent of which 611
  were identified inside the town of Tiburon. The depiction and use of town boundaries
  acquired from Wikimapia, are not warranted to be error- free nor do they imply official
  endorsement or acceptance by the United Nations. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-tiburon-town-and-surroundings]'
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
  description: UNOSAT analysts compared pre-event (17 July 2016) and post-event (17
    October 2016) WorldView-2 satellite imagery of Tiburon town to detect structural
    damage through visual change detection. The analysis identified 648 potentially
    damaged structures within the mapped area, of which 611 were located within Tiburon
    town boundaries, producing a post-disaster damage assessment dataset.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-tiburon-town-and-surroundings
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone assessed via satellite
      imagery change detection
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
  description: Haiti - Damage Assessment of Tiburon town and surroundings (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_gdb.zip
  format: Geodatabase
  id: resource_dbf1f088
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Damage Assessment of Tiburon town and surroundings (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_shp.zip
  format: null
  id: resource_9cb02996
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_unosat_damageassessmenttiburonto_20161027
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-27'
temporal_resolution: null
title: Haiti - Damage Assessment of Tiburon town and surroundings
version: null
vulnerability: null
---
