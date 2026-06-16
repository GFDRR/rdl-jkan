---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-3-grand-anse-and-sud-departements-haiti
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-3-grand-anse-and-sud-departements-haiti
dataset_id: rdls_hl-hti_unosat_preliminarybaseddamageass_20161124
description: 'This report describes preliminary building damage analysis carried out
  by UNITAR-UNOSAT covering Area 1 (Jeremie and Roseaux Commune), Area 2 (Abricot,
  Dame-Marie, Anse d''Hainaults and Les Irois Communes), Area 3 (Corail, Pestel, Beaumont
  and Roseaux Communes), and Area 4 (Tiburon Commune) for a total area of approximately
  1,200 Km2. Building damage analysis, including a rapid assessment of transportation
  network conditions and locations of spontaneous people gathering sites, was conducted
  by comparing the post-disaster satellite images (Pleiades acquired on 7/10/2016
  for AOI1, Pleiades acquired on 12/10/2016 for AOI2, Pleiades acquired on 09/11/2016
  for AOI3 and Worldview-2 acquired on 9/10/2016 & 17/10/2016 for AOI4) with available
  pre-disaster images (WorldView-1 on 08/12/2014, 01/05/2015, 09/05/2015 and 16/06/2015;
  Worldview-2 on 17/07/2016, 28/11/2014 and 14/06/2015 and Worldview-3 on 17/10/2015).
  UNOSAT''s preliminary analysis shows a total of 40,696 buildings/structures with
  visible damages and approximately 508 locations with visible road obstacles and/or
  access constraints. In addition, 1,497 temporary people gathering sites have been
  identified within the analysed areas (Area 1, Area 2, Area 3 and Area 4).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-3-grand-anse-and-sud-departements-haiti]'
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
  description: "UNOSAT analysts compared pre- and post-disaster Pleiades satellite\
    \ imagery acquired in October 2016 to conduct rapid damage assessment across four\
    \ communes in Grand Anse and Sud d\xE9partements, Haiti. Building damage and transportation\
    \ network conditions were identified through visual interpretation of notable\
    \ changes between satellite images, with results compiled into geodatabase and\
    \ shapefile formats for spatial analysis."
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
- href: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-3-grand-anse-and-sud-departements-haiti
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from tropical cyclone derived from
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Transportation network damage and disruption from tropical cyclone
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
  description: "Preliminary Satellite Based Damage Assessment Report - UPDATE 3: Grand\
    \ Anse and Sud D\xE9partements, Haiti (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003HTI_20161124.gdb.zip
  format: Geodatabase
  id: resource_8d1d3f9b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003HTI_20161124.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Preliminary Satellite Based Damage Assessment Report - UPDATE 3: Grand\
    \ Anse and Sud D\xE9partements, Haiti (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003HTI_20161124_SHP.zip
  format: null
  id: resource_64b93f9c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003HTI_20161124_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-hti_unosat_preliminarybaseddamageass_20161124
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
  start: '2016-11-24'
temporal_resolution: null
title: "Preliminary Satellite Based Damage Assessment Report - UPDATE 3: Grand Anse\
  \ and Sud D\xE9partements, Haiti"
version: null
vulnerability: null
---
