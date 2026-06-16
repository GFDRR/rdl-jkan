---
attributions:
- entity:
    affiliation: null
    email: jrc-risk-data-hub@ec.europa.eu
    name: European Commision (EC), Joint Research Centre (JRC)
    url: https://joint-research-centre.ec.europa.eu/
  id: Entity_1
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: estat-gisco@ec.europa.eu
  name: European Commission, Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
creator:
  affiliation: null
  email: estat-gisco@ec.europa.eu
  name: European Commission, Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
dataset_id: rdls_exp-jrc_drmkc_giscoairport
description: Europe dataset of airports
details: 'The dataset contains 3 feature classes with the location of over 11800 Pan
  European airports and heliports, plus one attribute table and 5 domain tables. The
  airports are identified using the International Civil Aviation Organisation (ICAO)
  airport codes. The dataset was first created as GISCO Airports 2006. It wasthenupdated
  in 2009 based on EuroRegionalMap (ERM) v3.0 from EuroGeographics. The GISCO Airports
  2013 dataset hosts three related feature classes: -AIRP_PT_2014: All airports and
  some heliports are represented by point topology, consisting of 11687 features.
  The point coordinates and most of the attributes in this feature class are based
  on the Eurocontrol database, complemented with other sources for the EU territories
  not covered by Eurocontrol.There are a number of basic attributes for each airport,
  such as different identification codes, airport name, altitude, etc.'
exposure:
- asset_type: null
  category: infrastructure
  id: exp_1
  metrics:
  - dimension: structure
    id: airport
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Commission, Eurostat/GISCO
    risk_data_type: null
    type: dataset
    url: https://ec.europa.eu/eurostat/web/gisco
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
publisher:
  affiliation: null
  email: null
  name: European Commission, Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
purpose: To provide a comprehensive europe dataset of airport and heliport locations
  with standardized ICAO codes and attributes for cartographic applications, spatial
  analysis, and aviation infrastructure planning.
referenced_by: []
resources:
- access_url: https://ec.europa.eu/eurostat/web/gisco/geodata/transport-networks
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4258
  description: The dataset contains 3 feature classes with the location of over 11800
    Pan European airports and heliports, plus one attribute table and 5 domain tables.
  download_url: https://ec.europa.eu/eurostat/cache/GISCO/geodatafiles/Airports-2013-SHP.zip
  format: null
  id: gisco_airport_2013
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Europe dataset of airports
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_drmkc_giscoairport
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: GISCO Europe Airports 2013
version: '2013'
vulnerability: null
---
