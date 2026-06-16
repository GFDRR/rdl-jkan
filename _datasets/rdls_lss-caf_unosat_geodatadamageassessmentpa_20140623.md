---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-paoua-ouhampende-central-african-republic-june-23-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-paoua-ouhampende-central-african-republic-june-23-2014
dataset_id: rdls_lss-caf_unosat_geodatadamageassessmentpa_20140623
description: 'This map illustrates locations of destroyed structures in the area of
  Paoua, Central African Republic. Using a satellite image acquired 18 June 2014 and
  compared to an image from 12 January 2012, UNOSAT reviewed the town of Paoua and
  surrounding areas to locate obvious signs of destroyed structures (see inset for
  example). An estimated total of 323 destroyed structures were located in the area
  as well as 25 possible damage structures, both in Paoua and in outlying towns and
  villages. The destroyed structures comprise an estimated 2.2% of the total number
  of pre-conflict structures in Paoua.Most destruction detected in the 18 June image
  was most likely a result of burning given the blackened structural remains visible
  in the imagery. This is a preliminary analysis and has not yet been validated in
  the field.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-paoua-ouhampende-central-african-republic-june-23-2014]'
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multitemporal satellite imagery (12 January
    2012 baseline vs. 18 June 2014 post-event) to identify and map destroyed structures
    through visual interpretation of notable changes in the urban landscape. A total
    of 323 destroyed structures and 25 possibly damaged structures were identified
    and georeferenced as point/polygon features.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-paoua-ouhampende-central-african-republic-june-23-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction identified
      through satellite imagery comparison
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
  description: Geodata of Damage Assessment in Paoua, OuhamPende, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF_shp.zip
  format: null
  id: resource_7e1bcfb2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment in Paoua, OuhamPende, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF.gdb.zip
  format: null
  id: resource_96497596
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_unosat_geodatadamageassessmentpa_20140623
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-06-23'
temporal_resolution: null
title: Geodata of Damage Assessment in Paoua, OuhamPende, Central African Republic
version: null
vulnerability: null
---
