---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2018-tropical-cyclone-sagar-path
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2018-tropical-cyclone-sagar-path
dataset_id: rdls_hl-som_icpac_2018tropicalcyclonesagarp_201805
description: 'This layer shows the movement path of 2018 Tropical Cyclone Sagar. Cyclone
  Sagar made landfall in north-western Somaliland on 19 May, 2018. It was a very rare
  cyclone in the Gulf of Aden. The storm moved with wind gusts of up to 120 km/hour
  that delivered a year&rsquo;s worth of rain to some areas, that is between 150 and
  200mm in some parts of the north. UNICEF was among the first to respond following
  the powerful tropical cyclone which caused death and widespread destruction in Hargeisa,
  Somaliland. As per UNICEF reports, some 170,000 were affected by Cyclone Sagar which
  hit the coast of north-western Somaliland and Djibouti on 18th May 2018 bringing
  heavy rains leading to flooding and adverse impacts. On 19th May 2018, Cyclone Sagar
  made landfall in western Somaliland, impacting close to 170,000 people, mainly in
  Awdal region. The floods in the south and the cyclone in the north destroyed crops,
  destroyed shelters and social service infrastructure, including water, health, nutrition,
  and education facilities. The Somaliland authorities estimated 50 people died and
  seven were still missing. In Somaliland, at least 16 people died in Galbeed and
  Awdal, where the cyclone made landfall. Three quarters of the livestock were killed
  along with major damage of water systems and health facilities and 39 schools were
  damaged or destroyed with a major impact on children. By the end of 2018, more than
  5.7 million people required basic health services, including critical needs in maternal
  and child health.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-2018-tropical-cyclone-sagar-path]'
details: null
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Observed tropical cyclone track data collected and compiled by ICPAC
    from meteorological monitoring during the May 2018 Cyclone Sagar event in the
    Gulf of Aden region. The dataset contains sequential position, wind speed, pressure,
    and directional information documenting the cyclone's movement from formation
    through landfall in Somaliland, integrated with reported impact data (affected
    population, casualties, damage) from UNICEF and other humanitarian sources.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-2018-tropical-cyclone-sagar-path
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Tropical Cyclone Sagar (170,000 affected)
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
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Widespread destruction to buildings and infrastructure from Cyclone
      Sagar
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
  - asset_category: population
    asset_dimension: population
    description: Deaths caused by Tropical Cyclone Sagar
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
        metric: casualty_count
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar0&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer shows the movement path of 2018 Tropical
    Cyclone Sagar. Cyclone Sagar made landfall in north-western Somaliland on 19 May,
    2018. It was a very rare cyclone in the Gulf of Aden. The storm moved with wind
    gusts of up to 120 km/hour that delivered a year&rsquo;s worth of rain to some
    areas, that is between 150 and 200mm in some parts of the north.
  download_url: null
  format: null
  id: resource_6968ba86
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2018 Tropical Cyclone Sagar Path Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar0&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer shows the movement path of 2018 Tropical Cyclone
    Sagar. Cyclone Sagar made landfall in north-western Somaliland on 19 May, 2018.
    It was a very rare cyclone in the Gulf of Aden. The storm moved with wind gusts
    of up to 120 km/hour that delivered a year&rsquo;s worth of rain to some areas,
    that is between 150 and 200mm in some parts of the north.
  download_url: null
  format: null
  id: resource_76353f25
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2018 Tropical Cyclone Sagar Path CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar0&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer shows the movement path of 2018 Tropical Cyclone
    Sagar. Cyclone Sagar made landfall in north-western Somaliland on 19 May, 2018.
    It was a very rare cyclone in the Gulf of Aden. The storm moved with wind gusts
    of up to 120 km/hour that delivered a year&rsquo;s worth of rain to some areas,
    that is between 150 and 200mm in some parts of the north.
  download_url: null
  format: null
  id: resource_28ae2061
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2018 Tropical Cyclone Sagar Path Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar0&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer shows the movement path of 2018 Tropical Cyclone
    Sagar. Cyclone Sagar made landfall in north-western Somaliland on 19 May, 2018.
    It was a very rare cyclone in the Gulf of Aden. The storm moved with wind gusts
    of up to 120 km/hour that delivered a year&rsquo;s worth of rain to some areas,
    that is between 150 and 200mm in some parts of the north.
  download_url: null
  format: null
  id: resource_e185db2b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2018 Tropical Cyclone Sagar Path GeoJSON
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_2018tropicalcyclonesagarp_201805
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
  end: '2018-05-20'
  start: '2018-05-19'
temporal_resolution: null
title: Somalia - 2018 Tropical Cyclone Sagar Path
version: null
vulnerability: null
---
