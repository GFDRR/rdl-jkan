---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: geodatarequest
  url: https://geonode.pacificdata.org/api/v2/users/1245
creator:
  affiliation: null
  email: null
  name: Pacific Community - SPC
  url: https://geonode.pacificdata.org/api/v2/users/1000
dataset_id: rdls_lss-wsm_pacificdata_annualaveragelossdistrict
description: 'The expected economic impact due to natural hazards is illustrated through
  an average annual loss (AAL) map, which indicates the estimated economic losses
  averaged over the 10,000 realizations of next-year activity. Economic loss is defined
  as the total direct ground-up losses, i.e., the cost needed to repair or replace
  damaged assets. Three types of assets were considered: (1) buildings (e.g., residential,
  commercial, industrial, and public buildings) - (2) major infrastructure (airports,
  ports, power plants, bridges, dams, etc.) - and (3) valuable crops (sugarcane, taro,
  rice, banana, etc.). Two types of natural events were explicitly considered in this
  risk analysis: earthquakes (inducing both ground shaking and tsunami waves) and
  tropical cyclones (inducing wind, precipitation/flood, and coastal flooding due
  to surge of the sea level). The resolution is taken at a specified administration
  boundary for each country. Compiled by AIR Worldwide. [Source: This metadata record
  was automatically extracted from GeoNode portal pacificdata]'
details: 'Methodology: Loss Earthquake Tsunami Cyclone Probabilistic Building Infrastructure
  Crops.'
exposure: []
hazard: null
license: CC-BY-NC-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/465
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of pluvial and coastal flood x buildings, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_flood_buildings
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of pluvial and coastal flood x major infrastructure, not a separate
      per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_flood_infrastructure
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of pluvial and coastal flood x crops, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_flood_agriculture
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of tropical cyclone wind x buildings, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: PGWS:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_strong_wind_buildings
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of tropical cyclone wind x major infrastructure, not a separate per-cell
      value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: PGWS:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_strong_wind_infrastructure
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of tropical cyclone wind x crops, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: PGWS:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_strong_wind_agriculture
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of earthquake ground shaking x buildings, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_buildings
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of earthquake ground shaking x major infrastructure, not a separate
      per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_infrastructure
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of earthquake ground shaking x crops, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_agriculture
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of tsunami x buildings, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: h_tsi:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_tsunami_buildings
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of tsunami x major infrastructure, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: h_tsi:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_tsunami_infrastructure
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Annual average loss (AAL) composite covering perils (pluvial and
      coastal flood, tropical cyclone wind, earthquake ground shaking, tsunami) and
      assets (buildings, major infrastructure, crops); the source value is a SINGLE
      aggregate and is NOT decomposed by peril or asset class. This entry documents
      coverage of tsunami x crops, not a separate per-cell value.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: h_tsi:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_tsunami_agriculture
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: judgement
      loss_frequency_type: probabilistic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/465
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Annual Average Loss at district level for Samoa (Zipped Shapefile)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aws_district_aal&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Annual Average Loss at district level for Samoa (GML 2.0)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aws_district_aal&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_1
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Annual Average Loss at district level for Samoa (Excel)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aws_district_aal&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Annual Average Loss at district level for Samoa (JSON)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aws_district_aal&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Annual Average Loss at district level for Samoa (GML 3.1.1)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aws_district_aal&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Annual Average Loss at district level for Samoa (CSV)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aws_district_aal&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: https://geonode.pacificdata.org/datasets/geonode:ws_district_aal
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Annual Average Loss at district level for Samoa (OGC WMS: geonode
    Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:ws_district_aal&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:ws_district_aal
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Annual Average Loss at district level for Samoa (OGC WFS: geonode
    Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:ws_district_aal&outputFormat=application%2Fjson
  format: null
  id: resource_7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-wsm_pacificdata_annualaveragelossdistrict
spatial:
  bbox:
  - -172.80309964585575
  - -14.07654578853517
  - -171.39852151415127
  - -13.438825731224375
  centroid: null
  countries:
  - WSM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Annual Average Loss at district level for Samoa
version: null
vulnerability: null
---
