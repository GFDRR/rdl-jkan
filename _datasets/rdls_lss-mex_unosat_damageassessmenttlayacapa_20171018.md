---
attributions:
- entity:
    affiliation: null
    email: null
    name: Institute of Geography of the National Autonomous University of Mexico (IGG-UNAM)
    url: https://data.humdata.org/dataset/damage-assessment-in-tlayacapan-town-municipality-of-tlayacapan-state-of-morelos-mexico-2707
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-tlayacapan-town-municipality-of-tlayacapan-state-of-morelos-mexico-2707
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-tlayacapan-town-municipality-of-tlayacapan-state-of-morelos-mexico-2707
dataset_id: rdls_lss-mex_unosat_damageassessmenttlayacapa_20171018
description: 'This map illustrates UAV images-detected and field work survey damaged
  structures in the town of Tlayacapan located in Tlayacapan Municipality, Morelos
  State, Mexico. The analyzed area is located at 68 km north-west of the epicentral
  zone of the 19 September 2017 M7.1 earthquake. The Institute of Geography of the
  National Autonomous University of Mexico (IGG-UNAM) identified 189 damaged structures.
  The analysis was performed using a post-event UAV images acquired on 7 October 2017
  and field work. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-in-tlayacapan-town-municipality-of-tlayacapan-state-of-morelos-mexico-2707]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Post-event damage assessment derived from UAV imagery acquired on 7
    October 2017 (18 days after the 19 September 2017 M7.1 earthquake) combined with
    field validation surveys. The Institute of Geography (IGG-UNAM) identified and
    classified 189 damaged structures in Tlayacapan town, located 68 km from the epicenter.
    UNOSAT compiled and standardized the results into geospatial vector datasets (geodatabase
    and shapefile formats) with damage classification attributes.
  sources:
  - id: source_1
    license: null
    name: Institute of Geography of the National Autonomous University of Mexico (IGG-UNAM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
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
- href: https://data.humdata.org/dataset/damage-assessment-in-tlayacapan-town-municipality-of-tlayacapan-state-of-morelos-mexico-2707
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 19 September 2017 M7.1 earthquake
      detected via UAV imagery and field survey
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Damage Assessment in Tlayacapan town, Municipality of Tlayacapan, State
    of Morelos, Mexico (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_682487b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Tlayacapan town, Municipality of Tlayacapan, State
    of Morelos, Mexico (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_4131e2e0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mex_unosat_damageassessmenttlayacapa_20171018
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-18'
temporal_resolution: null
title: Damage Assessment in Tlayacapan town, Municipality of Tlayacapan, State of
  Morelos, Mexico
version: null
vulnerability: null
---
