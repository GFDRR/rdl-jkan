---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-soaneriana-ivongo-district-analanjirofo-region-madagascar-2759
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-soaneriana-ivongo-district-analanjirofo-region-madagascar-2759
dataset_id: rdls_hl-mdg_unosat_detectedwatersextentsoane_20180110
description: 'This map illustrates satellite-detected water extent as of 09 January
  2018 over Soaneriana Ivongo district, Analanjirofo region, in Madagascar as detected
  by Radarsat-2. Limited standing waters can be observed in the area. These zones
  are mainly agricultural and/or swamps. These waters are the results of recent heavy
  rains following the cyclone AVA-18 which made landfall the 05 January 2018. It is
  likely that flood waters have been systematically underestimated along highly vegetated
  areas along main river banks and within built-up urban areas, due to the special
  characteristics of the satellite data used. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-soaneriana-ivongo-district-analanjirofo-region-madagascar-2759]'
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
  description: Radarsat-2 satellite imagery acquired on 09 January 2018 was analyzed
    by UNOSAT to detect water extent in Soaneriana Ivongo district following cyclone
    AVA-18 landfall on 05 January 2018. Multi-temporal image comparison identified
    standing water bodies in agricultural and swamp areas, with systematic underestimation
    acknowledged in vegetated riparian zones and urban areas due to radar signal penetration
    limitations.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-soaneriana-ivongo-district-analanjirofo-region-madagascar-2759
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Post-event satellite-detected water extent and inundation area in
      agricultural and swamp zones following cyclone-induced flooding
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
  description: Satellite Detected Waters Extent in Soaneriana Ivongo District, Analanjirofo
    Region, Madagascar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_gdb.zip
  format: Geodatabase
  id: resource_0e168c27
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20180103MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters Extent in Soaneriana Ivongo District, Analanjirofo
    Region, Madagascar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_shp.zip
  format: null
  id: resource_5a12b607
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20180103MDG_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mdg_unosat_detectedwatersextentsoane_20180110
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-01-10'
temporal_resolution: null
title: Satellite Detected Waters Extent in Soaneriana Ivongo District, Analanjirofo
  Region, Madagascar
version: null
vulnerability: null
---
