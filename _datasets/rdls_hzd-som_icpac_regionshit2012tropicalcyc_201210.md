---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2012-tropical-cyclone-murjan
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2012-tropical-cyclone-murjan
dataset_id: rdls_hzd-som_icpac_regionshit2012tropicalcyc_201210
description: 'On October 25, 2012 Cyclonic Storm Murjan struck Bayla District of eastern
  Somalia, bringing heavy rainfall of over 40 mm (1.6 in) and gusty winds to the country
  and neighboring Ethiopia. This layer shows the occurence of TC Murjan in Bari Region.
  TC Murjan formed over the south Arabian Sea in association with an active inter
  tropical convergence zone during last week of October 2012. It was the first cyclone
  over the north Indian Ocean during that year. Moving west southwestwards, it crossed
  Somalia coast between 1700 and 1800 UTC of 25th October near lat. 9.80N and long.
  50.80E. Though the Ocean Heat Content was less over the southwest Arabian Sea (50-80
  KJ/cm2) and further less near Somalia coast (less than 50 KJ/cm2) as well as SST
  (26-280C), the system could maintain its intensity of cyclonic storm till landfall,
  basically due to low to moderate vertical wind shear. TC Murjan brougt heavy rainfalls
  to Somalia. This resulted to flash flooding which washed away livestock and bridges
  in Bari region, causing some fatalities. A total of 100,000 livestock died. Districts
  impacted in the region included Bossasso, Ishkushban, Bandar Beyla, Garowe and Eyl
  Districts.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2012-tropical-cyclone-murjan]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event spatial dataset documenting the occurrence and geographic
    extent of Tropical Cyclone Murjan in Somalia's Bari Region on October 25, 2012.
    Data compiled by ICPAC from meteorological observations of the cyclone track,
    rainfall, and wind impacts, represented as administrative region polygons with
    event date and validation metadata.
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
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2012-tropical-cyclone-murjan
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TC_Murjan&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. On October 25, 2012 Cyclonic Storm Murjan struck Bayla District
    of eastern Somalia, bringing heavy rainfall of over 40 mm (1.6 in) and gusty winds
    to the country and neighboring Ethiopia. This layer shows the occurence of TC
    Murjan in Bari Region.
  download_url: null
  format: null
  id: resource_5aecd865
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2012 Tropical Cyclone Murjan CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TC_Murjan&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. On October 25, 2012 Cyclonic Storm Murjan struck Bayla
    District of eastern Somalia, bringing heavy rainfall of over 40 mm (1.6 in) and
    gusty winds to the country and neighboring Ethiopia. This layer shows the occurence
    of TC Murjan in Bari Region.
  download_url: null
  format: null
  id: resource_33300562
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2012 Tropical Cyclone Murjan Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TC_Murjan&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. On October 25, 2012 Cyclonic Storm Murjan struck Bayla
    District of eastern Somalia, bringing heavy rainfall of over 40 mm (1.6 in) and
    gusty winds to the country and neighboring Ethiopia. This layer shows the occurence
    of TC Murjan in Bari Region.
  download_url: null
  format: null
  id: resource_2302d763
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2012 Tropical Cyclone Murjan GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TC_Murjan&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. On October 25, 2012 Cyclonic Storm Murjan struck
    Bayla District of eastern Somalia, bringing heavy rainfall of over 40 mm (1.6
    in) and gusty winds to the country and neighboring Ethiopia. This layer shows
    the occurence of TC Murjan in Bari Region.
  download_url: null
  format: null
  id: resource_1b0e248b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2012 Tropical Cyclone Murjan Zipped Shapefile
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_icpac_regionshit2012tropicalcyc_201210
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
  end: '2012-10-25'
  start: '2012-10-23'
temporal_resolution: null
title: Somalia Regions hit by 2012 Tropical Cyclone Murjan
version: null
vulnerability: null
---
