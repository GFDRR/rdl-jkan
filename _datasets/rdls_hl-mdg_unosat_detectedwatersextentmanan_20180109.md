---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-mananjary-district-vatovavy-fitovinany-region-madagascar-2757
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-mananjary-district-vatovavy-fitovinany-region-madagascar-2757
dataset_id: rdls_hl-mdg_unosat_detectedwatersextentmanan_20180109
description: 'This map illustrates satellite-detected water extent as of 07 January
  2018 over Mananjary district, Vatovavy-Fitovinany region, in Madagascar as detected
  by Sentinel-1. ~ 1000 ha of land over the communes of Tsiatosika and ~1300 ha in
  Ankatafana seem to be inundated. These zones are mainly agricultural and/or swamps.
  These waters are the results of recent heavy rains following the cyclone AVA-18
  which made landfall the 05 January 2018. It is likely that flood waters have been
  systematically underestimated along highly vegetated areas along main river banks
  and within built-up urban areas, due to the special characteristics of the satellite
  data used. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-mananjary-district-vatovavy-fitovinany-region-madagascar-2757]'
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-1 synthetic aperture radar imagery
    acquired on 7 January 2018, comparing pre- and post-cyclone AVA-18 images to detect
    water extent changes. Water bodies were classified and mapped as vector polygons
    with area calculations in hectares, identifying ~2300 ha of inundation across
    agricultural and wetland zones in Mananjary district.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-mananjary-district-vatovavy-fitovinany-region-madagascar-2757
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct inundation of agricultural land and swamps totaling ~2300
      hectares across Tsiatosika and Ankatafana communes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Satellite Detected Waters Extent in Mananjary District, Vatovavy-Fitovinany
    Region, Madagascar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_gdb.zip
  format: Geodatabase
  id: resource_c42dc91e
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
  description: Satellite Detected Waters Extent in Mananjary District, Vatovavy-Fitovinany
    Region, Madagascar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_shp.zip
  format: null
  id: resource_a8930850
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
slug: rdls_hl-mdg_unosat_detectedwatersextentmanan_20180109
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
  start: '2018-01-09'
temporal_resolution: null
title: Satellite Detected Waters Extent in Mananjary District, Vatovavy-Fitovinany
  Region, Madagascar
version: null
vulnerability: null
---
