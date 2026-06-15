---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2013-somalia-tropical-cyclone-3a
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2013-somalia-tropical-cyclone-3a
dataset_id: rdls_hl-som_icpac_regionshit2013tropicalcyc_201311
description: 'Tropical Cyclone 3A was recorded on November 11, 2013 when a deep depression
  struck near the border of Nugaal and Bari regions and caused severe flash flooding.
  It was the deadliest tropical cyclone on record in Somalia.It formed off the north-east
  coast of Somalia across the Indian Ocean, moving directly towards the coast of the
  country. This cyclone had windspeeds of 74kph(46mph) and was characterized with
  rainfall amounts between (100-200)mm. The cyclone led to loss of human lives and
  destruction of assets including livestock and fishing boats. It destroyed numerous
  settlements, service centers, roads, schools, communication and electrical installations.
  The most affected areas included, Dangorayo, Bandar Beyla, Garowe and Eyl districts.
  Impacts can be summarized as follows: Number of People Affected: 142,380 Number
  of People worst affected: 8,523 Number of people displaced: 5,000 Number of people
  injured: 1,435 Number of death:100 Number of lost livestock: 2,746 Crop destroyed:12000ha.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2013-somalia-tropical-cyclone-3a]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event spatial dataset documenting the geographic extent of regions
    impacted by Tropical Cyclone 3A in November 2013. Administrative boundaries were
    overlaid with observed cyclone track and impact zones to delineate affected regions.
    The dataset integrates observed wind speeds (74 kph), rainfall measurements (100-200
    mm), and documented impacts including casualties, livestock losses, and settlement
    destruction.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2013-somalia-tropical-cyclone-3a
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct destruction of settlements and structures from tropical cyclone
      winds and associated flooding
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
  - asset_category: agriculture
    asset_dimension: product
    description: Direct loss of livestock and fishing boats from tropical cyclone
      impacts
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
          quantity_kind: area
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Loss of human lives from tropical cyclone 3A, recorded as deadliest
      tropical cyclone in Somalia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. Tropical Cyclone 3A was recorded on November 11, 2013 when
    a deep depression struck near the border of Nugaal and Bari regions and caused
    severe flash flooding. It was the deadliest tropical cyclone on record in Somalia.It
    formed off the north-east coast of Somalia across the Indian Ocean, moving directly
    towards the coast of the country. This cyclone had windspeeds of 74kph(46mph)
    and was characterized with rainfall amounts between (100-200)mm.
  download_url: null
  format: null
  id: resource_8d480c60
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2013 Somalia Tropical Cyclone 3A Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. Tropical Cyclone 3A was recorded on November
    11, 2013 when a deep depression struck near the border of Nugaal and Bari regions
    and caused severe flash flooding. It was the deadliest tropical cyclone on record
    in Somalia.It formed off the north-east coast of Somalia across the Indian Ocean,
    moving directly towards the coast of the country. This cyclone had windspeeds
    of 74kph(46mph) and was characterized with rainfall amounts between (100-200)mm.
  download_url: null
  format: null
  id: resource_cd7a9fc3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2013 Somalia Tropical Cyclone 3A Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. Tropical Cyclone 3A was recorded on November 11, 2013 when
    a deep depression struck near the border of Nugaal and Bari regions and caused
    severe flash flooding. It was the deadliest tropical cyclone on record in Somalia.It
    formed off the north-east coast of Somalia across the Indian Ocean, moving directly
    towards the coast of the country. This cyclone had windspeeds of 74kph(46mph)
    and was characterized with rainfall amounts between (100-200)mm.
  download_url: null
  format: null
  id: resource_4822c123
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2013 Somalia Tropical Cyclone 3A CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. Tropical Cyclone 3A was recorded on November 11, 2013
    when a deep depression struck near the border of Nugaal and Bari regions and caused
    severe flash flooding. It was the deadliest tropical cyclone on record in Somalia.It
    formed off the north-east coast of Somalia across the Indian Ocean, moving directly
    towards the coast of the country. This cyclone had windspeeds of 74kph(46mph)
    and was characterized with rainfall amounts between (100-200)mm.
  download_url: null
  format: null
  id: resource_8bc43658
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2013 Somalia Tropical Cyclone 3A GeoJSON
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_regionshit2013tropicalcyc_201311
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2013-11-12'
  start: '2013-11-10'
temporal_resolution: null
title: Somalia Regions hit by 2013 Somalia Tropical Cyclone 3A
version: null
vulnerability: null
---
